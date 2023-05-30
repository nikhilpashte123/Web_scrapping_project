# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 17:11:54 2023

@author: Admin
"""

import lxml
from bs4 import BeautifulSoup
import requests
import pandas as pd

for i in range(2,12):
    url="https://www.flipkart.com/search?q=mobiles+under+50000+rupees&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=relevance&page="+str(i)
    page=requests.get(url)
    content=page.content
    print(content)

    soup=BeautifulSoup(content,'lxml')
    box=soup.find('div',class_='_1YokD2 _3Mn1Gg')


    a=[]
    product_names=box.find_all('div',class_='_4rR01T')
    for i in product_names:
        a.append(i.text.strip())
    print(a)

    b=[]
    prices=box.find_all('div',class_='_30jeq3 _1_WHN1')
    for i in prices:
        b.append(i.text.strip())
    print(b)

    c=[]
    desc=box.find_all('ul',class_='_1xgFaf')
    for i in desc:
        c.append(i.text.strip())
    print(c)

    d=[]
    reviews=box.find_all('div',class_='_3LWZlK')
    for i in reviews:
        d.append(i.text.strip())
    print(d)

df=pd.DataFrame({"Product Name":a,"Prices":b,"Description":c,"Reviews":d})
print(df)

df.to_csv("C:\\Users\\Admin\\OneDrive\\Documents\\Scrapping Projects\\flipkartmobilesunder50k.csv")
