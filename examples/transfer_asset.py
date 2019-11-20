import achainpy.clachain
import achainpy.keys
from achainpy.types import Abi, Action
from achainpy.utils import parse_key_file
import os
import pytz
import json
import datetime as dt

# this url is to a testnet that may or may not be working.
# We suggest using a different testnet such as kylin or jungle
#
ca = achainpy.clachain.Clachain(url='http://127.0.0.1:8888')

arguments = {
    "from": "act",  # sender
    "to": "test",  # receiver
    "quantity": '1.0000 ACT',
    "memo": "Achain to the moon",
}
payload = {
    "account": "act.token",
    "name": "transfer",
    "authorization": [{
        "actor": "act",
        "permission": "owner",
    }],
}
#Converting payload to binary
data = ca.abi_json_to_bin(payload['account'], payload['name'], arguments)
#Inserting payload binary form as "data" field in original payload
payload['data'] = data['binargs']
#final transaction formed
trx = {"actions": [payload]}
#get expiration
trx['expiration'] = str(
    (dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))

key = achainpy.keys.ActKey('5JAaSV9atydvYzEdBErjVCVAtx2SYdo3PykoHwrtYA57Xk3QKgQ')
resp = ca.push_transaction(trx, key, broadcast=True)
print('***************************************************************')
print('***************************************************************')
print(resp)
print('***************************************************************')
print('***************************************************************')
print('transaction_id = ', resp['transaction_id'])
print('***************************************************************')
