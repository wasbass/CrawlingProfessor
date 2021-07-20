#import requests                 #這個套件比較便捷
#import urllib.request as req    #這個套件比較完整
from bs4 import BeautifulSoup as BS
#import csv
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

driver.find_element_by_id("email").clear()
driver.find_element_by_id("email").send_keys("waswang@gmail.com")
driver.find_element_by_id("pass").clear()
driver.find_element_by_id("pass").send_keys("")
driver.find_element_by_name("login").click()
time.sleep(3)

driver.get("https://www.facebook.com/phoenix.cheng.96")

def scroll(scrolltimes=1):
  for i in range(scrolltimes):
    #每一次頁面滾動都是滑到網站最下方
    js = 'window.scrollTo(0, document.body.scrollHeight);'
    driver.execute_script(js)
    print("+")
    time.sleep(3)

scroll(10)

soup = BS(driver.page_source, "html.parser")
aaa = soup.find_all("span" , class_ = "pcp91wgn")
print("總共抓到{}篇文".format(int(len(aaa)/2)))
i=0
for a in aaa:
  i += 1
  if not i%2:
    print(a.text)