import requests
from _local_settings import TINKOFF_API_KEY

#
#
# url = 'https://tqm-sme-integration.tinkoff.ru/import/call/with-file?apiVersion=1.0'
# headers = {
#     'accept': 'application/json',
#     'Authorization': f'Bearer {TINKOFF_API_KEY}',
# }
#
# files = {
#     'file': ('В 1712 году столица.mp3', open('В 1712 году столица.mp3', 'rb'), 'audio/mpeg'),
# }
#
# data = {
#     'value': '{"id": "123456", '
#              '"callDirection": "Inbound", '
#              '"startDate": "2023-07-20T15:50:34.761+03:00", '
#              '"endDate": "2023-07-20T15:51:44.761+03:00", '
#              '"hangupParty": "Client", '
#              '"operatorId": "743", '
#              '"operatorChannel": "Left", '
#              '"clientPhoneNumber": "+79819022105", '
#              '"reason": "cool some reason", '
#              '"result": "bool some result", '
#              '"languageCode": "Ru", '
#              '"taskType": "new"}'
# }
#
# response = requests.post(url, headers=headers, files=files, data=data)
# print(response.status_code)

url = 'https://tqm-sme.tinkoff.ru/bff-external-clients/task-tracker/tasks-list-by-evaluations'
headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer OcxkrOFzdALb7WubboufleAyhLc7MS3y',
    'Content-Type': 'application/json',
}

data = {
    'evaluationIds': [

    ]
}

response = requests.post(url, headers=headers, json=data)
print(response.json())

# url = 'https://tqm-sme.tinkoff.ru/rest/external-call/report/autoevaluations'
# headers = {
#     'Accept': 'application/json',
#     'Content-Type': 'application/json',
# }
#
# data = {
#     'startDate': '2023-07-20T10:15:22Z',
#     'endDate': '2023-07-20T23:15:22Z',
#     'operatorId': '743',
# }
#
# response = requests.post(url, headers=headers, json=data)
# print(response.status_code)
