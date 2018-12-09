import json
import requests

headers={'userkey':'4f17f9f7a7'}
url='http://www.lewei50.com/api/V1/gateway/updatelog/01'
def UpdateData():
    print('update data')
   #payload=[{'Name':'000001-VR','Value':'100'}]

    payload="[{'Name':'000001-VR','Value':'100'}]"

    r=requests.post(url,payload,headers=headers)
    #r=requests.post(url,json.dumps(payload),headers=headers)
    print (r.text)
    return("1")
def UpdateMessage():
    print('update message')
    payload={'Message':'it is ok'}
    r=requests.post(url,json.dumps(payload),headers=headers)
    print (r.text)
    return(1)
if __name__=='__main__':
    UpdateData()
