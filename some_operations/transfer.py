import achainpy.clachain
import achainpy.keys
from achainpy.types import Abi, Action
from achainpy.utils import parse_key_file
import os
import pytz
import json
import datetime as dt
import argparse


def console_print(data):
    print(json.dumps(data, indent=4))

parser = argparse.ArgumentParser(description='Command Line Interface to Achain via python')
parser.add_argument('--api-version','-v', type=str, default='v1', action='store', dest='api_version')
parser.add_argument('--url', '-u', type=str, action='store', default='https://127.0.0.1:8888', dest='url')
parser.add_argument('--time-out', type=int, action='store', default=30, dest='timeout')
subparsers = parser.add_subparsers(dest='subparser')
### transfer
trsnafer_parser = subparsers.add_parser('transfer')
trsnafer_parser.add_argument('sender', type=str, action='store', help='The account to transfer token')
trsnafer_parser.add_argument('key', type=str, action='store', help='The privite key of sender')
trsnafer_parser.add_argument('receiver', type=str, action='store', help='The account to receive the token')
trsnafer_parser.add_argument('quantity', type=str, action='store', help='The amount of the token to transfer, i.g "1.0000 ACT"')
trsnafer_parser.add_argument('--memo','-m', type=str, action='store', default='',help='The message of transfer token', dest='memo')
trsnafer_parser.add_argument('--code','-c', type=str, action='store', default='act.token',help='The code of this token belongs to',dest='code')

### create new asset
create_asset_parser = subparsers.add_parser('newasset')
create_asset_parser.add_argument('creator', type=str, action='store', help='The account to create new asset')
create_asset_parser.add_argument('count', type=str, action='store', help='The amount of the token to transfer, i.g "1.0000 ACT"')
create_asset_parser.add_argument('pkey', type=str, action='store', help='The privite key of sender')
create_asset_parser.add_argument('--code','-c', type=str, action='store', default='act.token',help='The code of this token belongs to',dest='mycode')
### issue
issue_parser = subparsers.add_parser('issue')
issue_parser.add_argument('issuer', type=str, action='store', help='The account to create new asset')
issue_parser.add_argument('amount', type=str, action='store', help='The amount of the token to transfer, i.g "1.0000 ACT"')
issue_parser.add_argument('issuekey', type=str, action='store', help='The privite key of sender')
issue_parser.add_argument('--code','-c', type=str, action='store', default='act.token',help='The code of this token belongs to',dest='issuecode')

### load contract
set_contract_parser = subparsers.add_parser('load')
set_contract_parser.add_argument('account', type=str, action='store', help='The account to set abi for')
set_contract_parser.add_argument('codep', type=str, action='store', help='The fullpath containing the contract code')
set_contract_parser.add_argument('abip', type=str, action='store', help='The fullpath containing the contract abo')
set_contract_parser.add_argument('setkey', type=str, action='store', help='Key to sign the transaction')
set_contract_parser.add_argument('--permission','-p', type=str, action='store', default='active', dest='permission')
# process args
args = parser.parse_args()
#

ca = achainpy.clachain.Clachain(url=args.url)
# run commands based on subparser
if args.subparser == 'transfer' :
    arguments = {"from": args.sender, "to": args.receiver, "quantity":  args.quantity,"memo": args.memo}
    payload = {"account": args.code, "name": "transfer","authorization": [{"actor": args.sender,"permission": "owner",}]}
    
    # print(arguments)
    # print(payload)
    #Converting payload to binary
    data = ca.abi_json_to_bin(payload['account'], payload['name'], arguments)
    #Inserting payload binary form as "data" field in original payload
    payload['data'] = data['binargs']
    #final transaction formed
    trx = {"actions": [payload]}
    #get expiration
    trx['expiration'] = str((dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))
    #get ActKey
    achainkey = achainpy.keys.ActKey(args.key)
    resp = ca.push_transaction(trx, achainkey, broadcast=True)
    console_print(resp)
elif args.subparser == 'newasset' :
    arguments = {"issuer": args.creator, "maximum_supply":  args.count}
    payload = {"account": args.mycode, "name": "create","authorization": [{"actor": args.creator,"permission": "owner",}]}
    data = ca.abi_json_to_bin(payload['account'], payload['name'], arguments)
    payload['data'] = data['binargs']
    trx = {"actions": [payload]}
    #get expiration
    trx['expiration'] = str((dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))
    #get ActKey
    achainkey = achainpy.keys.ActKey(args.pkey)
    resp = ca.push_transaction(trx, achainkey, broadcast=True)
    console_print(resp)
elif args.subparser == 'issue' :
    arguments = {"to": args.issuer, "quantity":  args.amount, "memo": "issue asset"}
    payload = {"account": args.issuecode, "name": "issue","authorization": [{"actor": args.issuer,"permission": "owner",}]}
    data = ca.abi_json_to_bin(payload['account'], payload['name'], arguments)
    payload['data'] = data['binargs']
    trx = {"actions": [payload]}
    #get expiration
    trx['expiration'] = str((dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))
    #get ActKey
    achainkey = achainpy.keys.ActKey(args.issuekey)
    resp = ca.push_transaction(trx, achainkey, broadcast=True)
    console_print(resp)
elif args.subparser == 'load' :
    ca.set_abi(args.account, args.permission, args.abip, args.setkey, True, 30)
    ca.set_code(args.account, args.permission, args.codep, args.setkey, True, 30)
    pass
