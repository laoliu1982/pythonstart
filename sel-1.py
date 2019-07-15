#coding:utf-8
import logging
import re
from selenium import webdriver
import json
import requests
import time
import chardet
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-gpu')
chrome_options.add_argument('--no-sandbox')
header={'userkey':'19c648c636'}
urldate='https://www.lewei50.com/api/V1/gateway/UpdateSensors/01'

urllog='https://www.lewei50.com/api/V1/gateway/Updatelog/01'
options=webdriver.FirefoxOptions()
print('x1')
options.add_argument('--headless')
print ('x2')
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s [line:%(lineno)d] [porcess:%(process)s] [thread:%(thread)s] %(message)s',datefmt='%Y-%m-%d %H:%M:%S',filename='mylog.log',filemode='a')
logging.info("abc")
try:
   # client=webdriver.Chrome(chrome_options=chrome_options)

    client=webdriver.Firefox(options=options)
    logging.info('hello')
    client.set_page_load_timeout(5)
    try:
        logging.info("get start")
        client.get("https://bj.lianjia.com/zufang")
        logging.info ("get stop")
        time.sleep(1)

    except Exception as e:
        logging.info(e)
        logging.info("11 except")
        client.execute_script("window.stop()")
    finally:
        x=client.find_element_by_css_selector("div.main-box.clear>div.con-box>div.list-head.clear>h2>span")
        logging.info(x.text)
        countSTR=x.text
        patten =re.compile(r'\d+')
        m=patten.search(countSTR)
        logging.info (m.group(0))
        payload=[{'name':'T1','value':m.group(0)}]
    try:   
        logging.info("do it again")
        client.get("https://bj.lianjia.com/zufang/rt1")
        logging.info("do it succeed")

    except Exception as e:
        logging.info(e)
        client.execute_script("window.stop()")
        logging.info("22 except")

    finally:
        x=client.find_element_by_css_selector("div.main-box.clear>div.con-box>div.list-head.clear>h2>span")
        logging.info(x.text)
        countSTR=x.text
        patten =re.compile(r'\d+')
        m=patten.search(countSTR)
        logging.info(m.group(0))

        payload.append({'name':'T2','value':m.group(0)})
        logging.info("before post")
        r=requests.post(urldate,json.dumps(payload),headers=header)
        logging.info(r.text)

except Exception as e:
    logging.info(e)
    logging.info("3 except")
    client.execute_script("window.stop()")
finally:
    client.quit()
    logging.info("end")
