from selenium import webdriver
import json
import time
import requests

payload_initial=[]
def lw_payload_append(name,payload,value):
    x={'name':name,'value':value}
    print(x)
    payload.append(x)
    print (payload)
    return(payload)
def lw_payload_upload(payload):
    header={'userkey':'19c648c636'}
    urldate='https://www.lewei50.com/api/V1/gateway/UpdateSensors/02'
    r=requests.post(urldate,json.dumps(payload),headers=header)
    print(r.text)

payload=lw_payload_append('z1',payload_initial,123)
lw_payload_upload(payload)

