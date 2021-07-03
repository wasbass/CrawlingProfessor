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

init_url = "http://www.econ.ntu.edu.tw"
init_sub = "/zh_tw/people/faculty0/faculty1/"

url = init_url + init_sub
res = req.Request(url , headers = {"User-Agent":host_key})

with req.urlopen(res) as response:
    data0 = response.read().decode('utf-8')

soup = BeautifulSoup(data0 , "html.parser")
profile_head = soup.find_all("ul",class_="i-member-profile-list")

L = []
L_suburl  = []
num = 0

for p0 in profile_head :
    head_data = p0.find( "span" , class_ = "i-member-value member-data-value-name")
    sub  = head_data.a.get("href")

    L_suburl.append(sub)
    num += 1

print("num = {}".format(num))

def get_text( profile , item : str ) -> str  :
    c = "member-data-value-" + item
    #print(c)

    try:
        t = profile.find("td" , class_ = c).text
    except:
        t = "NULL"
    return t

def intoCSV( L : list):
    with open(".\EconProfessors.csv", "a", newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file ,delimiter=',')
        writer.writerow(L)
        file.close() 

n = 0

for p1 in range(num):
    sub = L_suburl.pop(0)
    url = init_url + sub

    #print(url)

    res = req.Request(url , headers = {"User-Agent":host_key})
    with req.urlopen(res) as response:
        data1 = response.read().decode('utf-8')

    soup = BeautifulSoup(data1 , "html.parser")
    profile = soup.find("div",class_="show-member")
    
    name      = get_text(profile,"name")
    title     = get_text(profile,"job-title")
    expertise = get_text(profile,"research-expertise")
    edu       = get_text(profile,"education")
    web       = get_text(profile,"website")

    L = [name,title,expertise,edu,web]
    intoCSV(L)

    print("-", end = "")
    n += 1
    if n%10 == 0 :
        print( n ,"\n")

