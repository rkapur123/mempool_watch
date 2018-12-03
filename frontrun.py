import time
import random
import json
import requests


def send_request(request):
  url = 'http://localhost:8545'
  headers = {'content-type': 'application/json'}
  payload = {'jsonrpc': '2.0', 'id': random.randint(0, int(1e9))}
  payload.update(request)
  response = None
  while not response:
    try:
      response = requests.post(
          url, data=json.dumps(payload), headers=headers).json()
    except requests.exceptions.ConnectionError as e:
      pass
  if response['id'] != payload['id']:
    raise Exception('Returned mismatching id')
  try:
    return response['result']
  except KeyError:
    log('No result found!', response)
    raise Exception('No result returned')

def frontrun():
    new_filter_request = {
        'method': 'eth_newPendingTransactionFilter',
        'params': [],
    }
    filter_id = send_request(new_filter_request)
    log('Filter set:', filter_id)


frontrun();
