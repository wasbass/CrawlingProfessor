import urllib.request as req
from bs4 import BeautifulSoup
import webbrowser
import urllib
import csv
import numpy as np
import pandas as pd
import os
import time
import csv
import re

os.chdir("D:\python\gitrepo")
host_key = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36" #記得檢查甚麼意思

init_url = "http://www.econ.ntu.edu.tw/zh_tw/people/faculty0/faculty1"

res = req.Request(init_url , headers = {"User-Agent":host_key})

with req.urlopen(res) as response:
    data = response.read().decode('utf-8')

soup = BeautifulSoup(data , "html.parser")
print(soup)

profile_head = soup.find_all("ul",class_="i-member-profile-list")

for p0 in profile_head :
    head_data = p0.find( "span" , class_ = "i-member-value member-data-value-name")
    print(head_data.a.contents[0])


