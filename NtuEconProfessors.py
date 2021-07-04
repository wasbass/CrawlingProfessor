import urllib.request as req
from bs4 import BeautifulSoup
import os
import time
import csv

os.chdir("D:\python\gitrepo")
host_key = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"

###請求標頭（request header）含有能令網路協議同級層（peer）識別發出該用戶代理 (en-US)請求的軟體類型或版本號、該軟體使用的作業系統、還有軟體開發者的字詞串。
###網路瀏覽器常用的格式：User-Agent: Mozilla/<version> (<system-information>) <platform> (<platform-details>) <extensions>
###從開發人員工具-Network的html檔案中可以查到

init_url = "http://www.econ.ntu.edu.tw"
init_sub = "/zh_tw/people/faculty0/faculty1/"

url = init_url + init_sub
res = req.Request(url , headers = {"User-Agent":host_key})

with req.urlopen(res) as response:
    data0 = response.read().decode('utf-8')

soup = BeautifulSoup(data0 , "html.parser")
profile_head = soup.find_all("ul",class_="i-member-profile-list")

L_suburl = []
num = 0

for p0 in profile_head :
    head_data = p0.find( "span" , class_ = "i-member-value member-data-value-name")
    sub  = head_data.a.get("href")

    L_suburl.append(sub)
    num += 1

print("num = {}".format(num))

profile = ""

def get_text(item : str ) -> str  :
    global profile 
    c = "member-data-value-" + item
    try:
        t = profile.find("td" , class_ = c).text
    except:
        t = "NULL"
    return t

def intoCSV( L:list):
    with open(".\EconProfessors.csv", "a", newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file ,delimiter=',')
        writer.writerow(L)
        file.close() 

n = 0
for p1 in range(num):
    sub = L_suburl.pop(0)
    url = init_url + sub

    res = req.Request(url , headers = {"User-Agent":host_key})
    with req.urlopen(res) as response:
        data1 = response.read().decode('utf-8')

    soup = BeautifulSoup(data1 , "html.parser")
    profile = soup.find("div",class_="show-member")
    
    name      = get_text("name")
    title     = get_text("job-title")
    expertise = get_text("research-expertise")
    edu       = get_text("education")
    web       = get_text("website")

    L = [name,title,expertise,edu,web]
    intoCSV(L)

    print("-", end = "")
    n += 1
    if n%10 == 0 :
        print( n ,"\n")
    time.sleep(2)

