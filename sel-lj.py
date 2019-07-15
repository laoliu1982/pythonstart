from selenium import webdriver
import time 

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-gpu')

chrome_options.add_argument('--no-sandbox')

client=webdriver.Chrome(chrome_options=chrome_options)
client.get('https://bj.lianjia.com/zufang/rt200600000001')
time.sleep(1)
x=client.find_element_by_css_selector("div.content__article>p>span.content__title--hl")

print(x.text)
client.quit()
