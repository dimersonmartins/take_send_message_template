import json
import requests


async def send(data, authorizationKey):
    jsonData = json.dumps(data)
    return requests.post('https://http.msging.net/commands', data=jsonData, headers={'Content-Type': 'application/json',
                                                      'Authorization': authorizationKey})


async def sendMessage(data, authorizationKey):
    jsonData = json.dumps(data)
    return requests.post('https://http.msging.net/messages', data=jsonData, headers={'Content-Type': 'application/json',
                                                                                     'Authorization': authorizationKey})
