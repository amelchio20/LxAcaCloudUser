import boto3
import json
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

  print("Received event: " + json.dumps(event, indent=2))
  # message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])  
  
  nwhost = event['host']
  nwinterfacesip = event['interfaces']['ip']
  nwdns = event['interfaces']['dns']
  nwgroupid = event['groups']['groupid']
  nwtemplateid = event['templates']['templateid']
  
  print("nwhost: ", nwhost)
  print("nwinterfacesip: ", nwinterfacesip)
  print("nwdns: ", nwdns)
  print("nwgroupid:", nwgroupid)
  print("nwtemplateid: ", nwtemplateid)
  
  hosts = zapi.host.create(
    host=nwhost,
    status= 1,
    interfaces=[{
     "type": 1,
     "main": "1",
     "useip": 1,
     "ip": nwinterfacesip,
     "dns": nwdns,
     "port": 10050
    }],
    groups=[{
     "groupid": nwgroupid
    }],
    templates=[{
     "templateid": nwtemplateid
    }]
  )
  
  
  host_list = zapi.host.get(output="extend")
  info = json.dumps(host_list)
  res = json.loads(info)
  # print('item count:', len(res))
  allhosts = dict()
  for item in res:
    # print("ITEM-LINE:", item)
    # print("----------------------------------------------------------------")
    allhosts.update({item['hostid']:item['host']})
    # print('hostid: ' + item['hostid'] + '  host: ' + item['host'])
    # print("----------------------------------------------------------------")
  
  print(allhosts)
  
  

  bucket = 's3-ec2-terraform-states'
  writefile = 'zabbix/id-host-list.json'
   
  s3 = boto3.resource('s3')
  s3object = s3.Object(bucket, writefile)
   
  s3object.put(
      Body=(bytes(json.dumps(allhosts).encode('UTF-8')))
  )

