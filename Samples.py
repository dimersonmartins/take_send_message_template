import time
import asyncio
import Widget as Take

# toronto_rico_quer_receber_tips
# toronto_rico_tip_pontual


async def FirstMessage(phoneNumber, nome):
    widget = Take.Widget(
        authorizationKey='Key dGFrZWNlbHVsYXRvcm9udG86dk16MGRSaVRueDd3OEZnSEVXOXU=',
        channel='ricozaptips2@msging.net',
        blockId='c0810898-3c36-4604-a13c-389757cefe68',
        stateid='a2217b96-6069-4b6e-b81b-c3b12bbe850d',
        templateName='toronto_rico_tip_pontual',
        templateNamespace='1516c70a_3045_4ae9_b2b4_67de2e4bad10',
        phoneNumber=phoneNumber)

    await widget.SendMessageTemplate(parameters=[nome])
    await widget.ChangeMasterState()
    await widget.ChangeUserState()


async def TipMessage(phoneNumber):
    widget = Take.Widget(
        authorizationKey='Key dGFrZWNlbHVsYXRvcm9udG86dk16MGRSaVRueDd3OEZnSEVXOXU=',
        channel='ricozaptips2@msging.net',
        blockId='aaa92fdc-ca67-4228-a8be-052eedcba905',
        stateid='a2217b96-6069-4b6e-b81b-c3b12bbe850d',
        templateName='toronto_dica_do_dia',
        templateNamespace='1516c70a_3045_4ae9_b2b4_67de2e4bad10',
        phoneNumber=phoneNumber)

    await widget.SendMessageTemplate(parameters=[
        "Seu resultado bruto diário médio nos trades em minicontratos foi de R$ 58,56. No entanto, na segunda-feira passada (04/10/2021), seu resultado foi de R$ 5.445,00. O seu número médio de contratos operados era de aproximadamente 165 considerando seus dias de operações desde 01/10/2019. Mas, na segunda-feira passada (04/10/2021), você operou 2802 minicontratos, que é um número significativamente maior. Tenha muito cuidado durante suas operações, lembre-se que que o seu Plano de trading é seu principal aliado.",
        "Footer"], tip=True)

    await widget.ChangeMasterState()
    await widget.ChangeUserState()
    await widget.SetStorageContact({
        "name": "Dica de ouro",
        "content": "Seu resultado bruto diário médio nos trades em minicontratos foi de R$ 58,56. No entanto, na segunda-feira passada (04/10/2021), seu resultado foi de R$ 5.445,00. O seu número médio de contratos operados era de aproximadamente 165 considerando seus dias de operações desde 01/10/2019. Mas, na segunda-feira passada (04/10/2021), você operou 2802 minicontratos, que é um número significativamente maior. Tenha muito cuidado durante suas operações, lembre-se que que o seu Plano de trading é seu principal aliado."
    })


async def LastMessage(phoneNumber, nome):
    widget = Take.Widget(
        authorizationKey='Key dGFrZWNlbHVsYXRvcm9udG86dk16MGRSaVRueDd3OEZnSEVXOXU=',
        channel='ricozaptips2@msging.net',
        blockId='fb54bc17-e1e7-409c-9cd6-db19ab6c4160',
        stateid='a2217b96-6069-4b6e-b81b-c3b12bbe850d',
        phoneNumber=phoneNumber)

    message = "Olá, *"+nome+"!*\n\n"
    message += "Parabéns!!! \n\n"
    message += "Me ajude a enviar dicas cada vez melhores!\n\n"
    message += "Se você pudesse dar uma dica para si mesmo durante o dia de hoje, o que gostaria de falar?\n\n"
    message += "*(escreva em apenas uma mensagem)*"

    await widget.SendMessage(message=message)
    await widget.ChangeMasterState()
    await widget.ChangeUserState()

# 11949128972 envia mensagem para o numero da célula
async def Proccess():
    await FirstMessage("5511914815000","Dimerson")
    await FirstMessage("555199049449","Gustavo")
    await FirstMessage("5511994880655","Gustavo")
    time.sleep(60)
    await TipMessage("5511914815000")
    await TipMessage("555199049449")
    await TipMessage("5511994880655")
    time.sleep(60)
    await LastMessage("5511914815000","Dimerson Daniel")
    await LastMessage("555199049449","Gustavo")
    await LastMessage("5511994880655","Gustavo")

asyncio.run(Proccess())
