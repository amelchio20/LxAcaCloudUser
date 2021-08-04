import boto3
import requests
from pyzabbix import ZabbixAPI

def lambda_handler(event, context):
  ssm = boto3.client('ssm')

  parameter = ssm.get_parameter(Name='/dev/zabbix/api/url', WithDecryption=True)
  url = parameter['Parameter']['Value']

  parameter = ssm.get_parameter(Name='/dev/zabbix/api/username', WithDecryption=True)
  user = parameter['Parameter']['Value']

  parameter = ssm.get_parameter(Name='/dev/zabbix/api/password', WithDecryption=True)
  pwd = parameter['Parameter']['Value']

  ZABBIX_SERVER = url
  zapi = ZabbixAPI(ZABBIX_SERVER)

  zapi.login(user, pwd)

  host_list = zapi.host.get(
    output="extend",
  )
  print(host_list)
