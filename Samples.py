import time
import asyncio
import Widget as Take

async def FirstMessage(phoneNumber, nome):
    widget = Take.Widget(
        authorizationKey='Key ',
        channel='channel@msging.net',
        blockId='blockId-3c36-4604-a13c-389757cefe68',
        stateid='stateid-6069-4b6e-b81b-c3b12bbe850d',
        templateName='templateName',
        templateNamespace='templateNamespace',
        phoneNumber=phoneNumber)

    await widget.SendMessageTemplate(parameters=[nome])
    await widget.ChangeMasterState()
    await widget.ChangeUserState()


async def TipMessage(phoneNumber):
    widget = Take.Widget(
        authorizationKey='Key ',
        channel='channel@msging.net',
        blockId='blockId-3c36-4604-a13c-389757cefe68',
        stateid='stateid-6069-4b6e-b81b-c3b12bbe850d',
        templateName='templateName',
        templateNamespace='templateNamespace',
        phoneNumber=phoneNumber)

    await widget.SendMessageTemplate(parameters=[
        "Tip",
        "Footer"], tip=True)

    await widget.ChangeMasterState()
    await widget.ChangeUserState()
    await widget.SetStorageContact({
        "name": "TipName",
        "content": "Tip"
    })


async def LastMessage(phoneNumber, nome):
    widget = Take.Widget(
        authorizationKey='Key =',
        channel='channel@msging.net',
        blockId='blockId-3c36-4604-a13c-389757cefe68',
        stateid='stateid-6069-4b6e-b81b-c3b12bbe850d',
        phoneNumber=phoneNumber)

    message = "Olá, *"+nome+"!*\n\n"

    await widget.SendMessage(message=message)
    await widget.ChangeMasterState()
    await widget.ChangeUserState()

async def Proccess():
    await FirstMessage("5551999999999", "Contact Name")
    time.sleep(60)
    await TipMessage("5551999999999")
    time.sleep(60)
    await LastMessage("5551999999999", "Contact Name")

asyncio.run(Proccess())
