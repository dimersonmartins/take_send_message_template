import uuid
from datetime import datetime
import Commands as CMD
import Console


class Widget:
    def __init__(self, authorizationKey, phoneNumber, channel='', stateid='', blockId='', templateName='', templateNamespace='', contactName=''):
        self.AuthorizationKey = authorizationKey
        self.PhoneNumber = phoneNumber
        self.Channel = channel
        self.Stateid = stateid
        self.BlockId = blockId
        self.TemplateName = templateName
        self.TemplateNamespace = templateNamespace
        self.AlternativeAccount = ''
        self.TipName = ''
        self.ContactName = contactName

    def Guid(self):
        return str(uuid.uuid4())

    async def GetAlternativeAccount(self):
        resp = {'': ""}
        try:
            Console.Header('Get alternative account')

            resp = await CMD.send({
                "id": self.Guid(),
                "to": "postmaster@wa.gw.msging.net",
                "method": "get",
                "uri": "lime://wa.gw.msging.net/accounts/+"+self.PhoneNumber
            }, self.AuthorizationKey)

            self.AlternativeAccount = resp.json(
            )['resource']['alternativeAccount']

            Console.Success('Alternative account ' + self.AlternativeAccount)
        except:
            Console.Error('Error alternative account')

    async def ChangeMasterState(self):
        try:
            Console.Header('Change master state')

            if(self.AlternativeAccount):
                self.AlternativeAccount = self.AlternativeAccount
            else:
                self.AlternativeAccount = self.PhoneNumber+"@wa.gw.msging.net"

            await CMD.send({
                "id": self.Guid(),
                "to": "postmaster@msging.net",
                "method": "set",
                "uri": "/contexts/"+self.AlternativeAccount+"/master-state",
                "type": "text/plain",
                "resource": self.Channel
            }, self.AuthorizationKey)

            Console.Success('Success Change master state')

        except:
            Console.Error('Error Change master state')

    async def ChangeUserState(self):
        try:
            Console.Header('Change user state')

            if(self.AlternativeAccount):
                self.AlternativeAccount = self.AlternativeAccount
            else:
                self.AlternativeAccount = self.PhoneNumber+"@wa.gw.msging.net"

            await CMD.send({
                "id": self.Guid(),
                "method": "set",
                "uri": "/contexts/"+self.AlternativeAccount+"/stateid@"+self.Stateid,
                "type": "text/plain",
                "resource": self.BlockId
            }, self.AuthorizationKey)

            Console.Success('Success Change user state')

        except:
            Console.Error('Error Change user state')

    async def SendMessageTemplate(self, parameters=[], tip=False):
        try:

            Console.Header('Send Message Template')
            await self.GetAlternativeAccount()

            storage = await self.GetStorageContact()
            storage = storage.json()

            if(tip):
                if(storage['resource']['actions'] and 'false' in storage['resource']['actions']['receive'] or 'none' in storage['resource']['actions']['receive']):
                    return

            if(not tip):
                action = str(datetime.now()) + " | " + \
                    self.AlternativeAccount + " | " + self.TemplateName
                await self.EventTrack("Comeco do dia menu detalhes do envio", action)

            _parameters = []
            for content in parameters:
                _parameters.append({"type": "text", "text": content})

            data = {
                "id": self.Guid(),
                "to": self.AlternativeAccount,
                "type": "application/json",
                "content": {
                    "type": "template",
                    "template": {
                        "namespace":  self.TemplateNamespace,
                        "name":  self.TemplateName,
                        "language": {
                            "code": "pt_BR",
                            "policy": "deterministic"
                        },
                        "components": [
                            {
                                "type": "body",
                                "parameters": _parameters
                            }
                        ]
                    }
                }
            }

            await CMD.sendMessage(data, self.AuthorizationKey)

            Console.Success('Success Send Message Template')
        except:
            Console.Error('Error Send Message Template')

    async def SendMessage(self, tip=False):
        try:
            await self.GetAlternativeAccount()

            if(tip):
                storage = await self.GetStorageContact()
                storage = storage.json()
                if(storage['resource']['actions'] and 'false' in storage['resource']['actions']['receive'] or 'none' in storage['resource']['actions']['receive']):
                    return

            Console.Header('Send Message')

            message = "Ol??, *"+self.ContactName+"!*\n\n"
            message += "Parab??ns!!! \n\n"
            message += "Me ajude a enviar dicas cada vez melhores!\n\n"
            message += "Se voc?? pudesse dar uma dica para si mesmo durante o dia de hoje, o que gostaria de falar?\n\n"
            message += "*(escreva em apenas uma mensagem)*"

            await CMD.sendMessage({
                "id": self.Guid(),
                "to": self.AlternativeAccount,
                "type": "text/plain",
                "content": message
            }, self.AuthorizationKey)

            action = str(datetime.now()) + " | " + self.AlternativeAccount
            await self.EventTrack("Final do dia me ajude a enviar dicas detalhes envio", action)

            Console.Success('Success Send Message Template')
        except:
            Console.Error('Error Send Message Template')

    async def GetStorageContact(self):
        try:
            Console.Header('Get storage contact ' + self.PhoneNumber)
            if(self.AlternativeAccount):
                self.AlternativeAccount = self.AlternativeAccount
            else:
                self.AlternativeAccount = self.PhoneNumber+"@wa.gw.msging.net"

            resp = await CMD.send({
                "id": self.Guid(),
                "method": "get",
                "uri": "/buckets/"+self.AlternativeAccount+"@storage"
            }, self.AuthorizationKey)

            Console.Success('Success Get storage contact')
            return resp
        except:
            Console.Error('Error Get storage contact')

    async def SetStorageContact(self, tip):
        try:
            Console.Header('Set storage contact ' + self.PhoneNumber)
            if(self.AlternativeAccount):
                self.AlternativeAccount = self.AlternativeAccount
            else:
                self.AlternativeAccount = self.PhoneNumber+"@wa.gw.msging.net"

            tipId = self.Guid()
            tip['id'] = tipId

            storage = await self.GetStorageContact()
            storage = storage.json()
            resource = {}
            contentArray = []
            if('success' in storage['status']):
                resource = storage['resource']
                if(resource['data']):
                    contentArray = resource['data']
                    contentArray.append(tip)
                    resource['data'] = contentArray
                    resource['actions']['lastTip'] = tip['name']
                    resource['actions']['likedIt'] = 'none'
                else:
                    contentArray.append(tip)
                    resource['data'] = contentArray
                    resource['actions']['lastTip'] = tip['name']
                    resource['actions']['likedIt'] = 'none'
            else:
                contentArray.append(tip)
                resource = {
                    "actions": {
                        "lastTip": tip['name'],
                        "receive": 'none',
                        "likedIt": 'none',
                    },
                    "lastInput": "",
                    'data': contentArray
                }

            action = str(datetime.now()) + " | " + tipId + " | " + \
                tip['name'] + " | " + self.AlternativeAccount + \
                " | " + self.TemplateName

            await self.EventTrack("Dica menu detalhes do envio", action)

            await CMD.send({
                "id": self.Guid(),
                "method": "set",
                "uri": "/buckets/"+self.AlternativeAccount+"@storage",
                "type": "application/x-my-type+json",
                "resource": resource
            }, self.AuthorizationKey)

            Console.Success('Success Set storage contact')
        except:
            Console.Error('Error Set storage contact')

    async def EventTrack(self, category, action):
        try:
            Console.Header('Set Event Track ' + self.PhoneNumber)

            if(self.AlternativeAccount):
                self.AlternativeAccount = self.AlternativeAccount
            else:
                self.AlternativeAccount = self.PhoneNumber+"@wa.gw.msging.net"

            resp = await CMD.send({
                "id": self.Guid(),
                "to": "postmaster@analytics.msging.net",
                "method": "set",
                "type": "application/vnd.iris.eventTrack+json",
                "uri": "/event-track",
                "resource": {
                    "category": category,
                    "action": action
                }
            }, self.AuthorizationKey)

            Console.Success('Success Set Event Track')
            return resp
        except:
            Console.Error('Error Set Event Track')
