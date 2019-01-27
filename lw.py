import requests
import json
class lewei50():
    def __init__(self,userkey,gw):
        self.userkey=userkey
        self.UploadPayload=[]
        self.gw=gw
    def UpdateMessage(self,message):
        JsonMessage={}
        JsonHeader={}
        JsonMessage['Message']=message
        JsonHeader['userkey']=self.userkey
        print (JsonHeader)
        url='http://www.lewei50.com/api/V1/gateway/updatelog/'+self.gw
        UploadMessage=json.dumps(JsonMessage)

        r=requests.post(url,UploadMessage,headers=JsonHeader)
        print (r.text)



    def print_all(self):
        print('the userkey is %s' %self.userkey)
        print('the  gw is %s' %self.gw)
        print ('the UploadMessage is %s' %json.dumps(self.UploadMessage))
   
    
