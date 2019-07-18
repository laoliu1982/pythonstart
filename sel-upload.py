from selenium import webdriver
import lw
import time 

chrome_options=webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-gpu')

chrome_options.add_argument('--no-sandbox')

client=webdriver.Chrome(chrome_options=chrome_options)

#client.header_overridesr={'Authorization':'Basic YWRtaW46YWRtaW4=',}
while (1):

    client.get('http://admin:admin@192.168.1.6/monitor.html')
    time.sleep(1)
    x=client.find_element_by_css_selector("#last_update")
    y=lw.lewei50('19c648c636','01')
    y.UpdateSensor('time',x.text)
    print(x.text)
    time.sleep(15)
    y.UploadSensor()
client.quit()
