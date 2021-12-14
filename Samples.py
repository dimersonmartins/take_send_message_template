import time
from datetime import datetime
import asyncio
import Widget as Take


async def FirstMessage(phoneNumber, nome):
    widget = Take.Widget(
        authorizationKey='Key',
        channel='channel@msging.net',
        blockId='blockId',
        stateid='stateid',
        templateName='templateName',
        templateNamespace='templateNamespace',
        phoneNumber=phoneNumber)

    await widget.SendMessageTemplate(parameters=[nome])
    await widget.ChangeMasterState()
    await widget.ChangeUserState()


async def TipMessage(phoneNumber):
    widget = Take.Widget(
        authorizationKey='Key',
        channel='channel@msging.net',
        blockId='blockId',
        stateid='stateid',
        templateName='templateName',
        templateNamespace='templateNamespace',
        phoneNumber=phoneNumber)

    await widget.SendMessageTemplate(parameters=[
        "Message content",
        "Footer"], tip=True)

    await widget.ChangeMasterState()
    await widget.ChangeUserState()
    await widget.SetStorageContact({
        "name": "tip name",
        "content": "content"
    })


async def LastMessage(phoneNumber, nome):
    widget = Take.Widget(
        authorizationKey='Key',
        channel='channel@msging.net',
        blockId='blockId',
        stateid='stateid',
        phoneNumber=phoneNumber)
    
    await widget.SendMessage(message="message")
    await widget.ChangeMasterState()
    await widget.ChangeUserState()


async def Proccess():
    await FirstMessage("5551999999999", "Name")
    time.sleep(10)
    await TipMessage("5551999999999")
    time.sleep(10)
    await LastMessage("5551999999999", "Name")

asyncio.run(Proccess())
