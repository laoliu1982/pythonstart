import requests
import json
class lewei50():
    def __init__(self,userkey,gw):
        self.userkey=userkey
        self.UploadPayload=[]
        self.gw=gw
        self.sensor=[]
        self.logurl='http://www.lewei50.com/api/V1/gateway/updatelog/'+self.gw

        self.sensorurl='http://www.lewei50.com/api/V1/gateway/UpdateSensors/'+self.gw
        self.JsonHeader={'userkey':userkey}

    def UploadMessage(self,message):
        JsonMessage={'Message':message}
        UploadMessage=json.dumps(JsonMessage)

        r=requests.post(self.logurl,UploadMessage,headers=self.JsonHeader)
        print (r.text)
    def UpdateSensor(self,name,value):
        SensorDict={}
        SensorDict['Name']=name
        SensorDict['Value']=value
        self.sensor.append(SensorDict)
        print (self.sensor)
    def UploadSensor(self):
        r=requests.post(self.sensorurl,json.dumps(self.sensor),headers=self.JsonHeader)
        print(r.text)


    def print_all(self):
        print('the userkey is %s' %self.userkey)
        print('the  gw is %s' %self.gw)
        print ('the UploadMessage is %s' %json.dumps(self.UploadMessage))
   
    
