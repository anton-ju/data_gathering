# -*- coding: utf-8 -*-
"""
Created on Wed Apr 09 17:34:38 2014

@author: ThaiSSD
"""
import requests
from bs4 import BeautifulSoup
#import urllib3
import re


doc = requests.get("https://www.avito.ru/sankt-peterburg/avtomobili/bmw")

#print(doc.text)

soup = BeautifulSoup(doc.text, "lxml")

table1 = soup.find_all(attrs={'class':'item-description-title-link'})
table2 = soup.find_all(attrs={'class':'about'})

item_list = []



li1 = [_.text for _ in table1]
li2 = [_.text for _ in table2]

for i in range(len(li1)):
    
    if li2[i].find('Битый') :
        broken = True
        li2[i] = li2[i].replace('Битый,', '')
        
    data_item = [_.replace('\n','') for _ in li1[i].split(',')] + [_.replace('\n','') for _ in li2[i].split(',')]
    model = ''.join(data_item[0].strip(' '))
    year = ''.join(data_item[1].strip(' '))
    prise_km = [_.strip(' \xa0км') for _ in (data_item[2].split('руб.'))], data_item[2]
    prise = prise_km[0]
    km = prise_km[1]
    volume_power = data_item[3].split(' ')
    volume = volume_power[0]
    transmission = volume_power[1]
    power = volume_power[2].strip('(')
    print(volume_power[1].split(' \xa0('))
#    , volume, transmission, power)
#    item_list.append([])
        
#print(li2[46])
#print(item_list[49][1])
