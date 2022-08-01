#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:38:23 2021

@author: tom
"""


from selenium import webdriver
import time
#bs4 html decomposer#
from bs4 import BeautifulSoup

import re
import sys
import string
import lxml
import socket
import os
#from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

### Create Text to store scraped data ##

## Create variable that looks up the chrome driver library ##
import os
import re
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from urllib.parse import urljoin
from bs4 import BeautifulSoup

binary = "/home/tom/Downloads/chromedriver_linux64/chromedriver"
#from selenium.webdriver.chrome.options import Option
#os.environ["webdriver.chrome.driver"] = chromedriver

# options = webdriver.Options()
# options.add_extension('./extensions/Disable-HTML5-Autoplay_v0.6.2.crx')
# options.add_extension('./extensions/AdBlock_v3.8.8.crx')

### Create Text file and structure the headers to which we will write the roster data ##
# Sport = open("SideArm_Rosters_2018.txt", 'w')
### Create the header for the text file ##
# Sport_Header = 'School'+';'+'Name'+';'+'Pos'+';'+'Ht'+';'+'Class'+';'+'Hometown'+';'+'Previous'+';'+'HomePrev'+';'+'HomeHS'+'\n'
# Sport.write(Sport_Header)

## initiate driver and get the old url ##
driver = webdriver.Chrome(binary)
url = 'https://www.footballoutsiders.com/stats/nfl/historical-lookup-by-week/2006/1/offense'
        
## fetch page and let it load ##
driver.get(url)
#delay = 5
import time
import pandas as pd
from bs4 import BeautifulSoup

import re
import sys
import string
import lxml
import socket
import os
import urllib
import csv
import time
from random import randint

#from pathlib import Path

#os.path.realpath('.')

year=['2021']#,'2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
week=['1','2','3','4','5','6','7','8','9','10','11','12']#,'5','6','7','8','9','10','11','12','13','14','15','16','17']
lst=[]
for yr in year:
    for wk in week:
        time.sleep(randint(1,3))
        url = 'https://www.footballoutsiders.com/stats/nfl/historical-lookup-by-week/{}/{}/offense'.format(yr, wk)
        
## fetch page and let it load ##
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml", from_encoding="utf-8")

        
        tre = soup.find_all('tr', {'class':'even'})
        tro = soup.find_all('tr', {'class':'odd'})
        
        for d in tre:
            td = d.find_all('td')
            for ds in td:
                try:
                    td0 = td[0].text
                except IndexError:
                    td0 = ''
                try:
                    td1 = td[1].text
                except IndexError:
                    td1 = ''
                try:
                    td2 = td[2].text
                except IndexError:
                    td2 =''
                try:
                    td3 = td[3].text.replace("%","")
                except IndexError:
                    td3 = ''
                try:
                    td4 = td[4].text
                except IndexError:
                    td4 =''
                try:
                    td5 = td[5].text.replace("%","")
                except IndexError:
                    td5 = ''
                try:
                    td6 = td[6].text
                except IndexError:
                    td6=''
                try:
                    td7 = td[7].text.replace("%","")
                except IndexError:
                    td7=''
                try:
                    td8 = td[8].text
                except IndexError:
                    td8 = ''
                try:
                    td9 = td[9].text.replace("%","")
                except IndexError:
                    td9 = ''
            bring = str(yr)+';'+str(wk)+';'+td0+';'+td1+';'+td2+';'+td3+';'+td4+';'+td5+';'+td6+';'+td7+';'+td8+';'+td9+'\n'
            lst.append(bring)
            print(bring)
        
        for d in tro:
            td = d.find_all('td')
            for ds in td:
                try:
                    td0 = td[0].text
                except IndexError:
                    td0 = ''
                try:
                    td1 = td[1].text
                except IndexError:
                    td1 = ''
                try:
                    td2 = td[2].text
                except IndexError:
                    td2 =''
                try:
                    td3 = td[3].text.replace("%","")
                except IndexError:
                    td3 = ''
                try:
                    td4 = td[4].text
                except IndexError:
                    td4 =''
                try:
                    td5 = td[5].text.replace("%","")
                except IndexError:
                    td5 = ''
                try:
                    td6 = td[6].text
                except IndexError:
                    td6=''
                try:
                    td7 = td[7].text.replace("%","")
                except IndexError:
                    td7=''
                try:
                    td8 = td[8].text
                except IndexError:
                    td8 = ''
                try:
                    td9 = td[9].text.replace("%","")
                except IndexError:
                    td9 = ''
            bring = str(yr)+';'+str(wk)+';'+td0+';'+td1+';'+td2+';'+td3+';'+td4+';'+td5+';'+td6+';'+td7+';'+td8+';'+td9+'\n'
            lst.append(bring)
            print(bring)

df = pd.DataFrame([sub.split(";") for sub in lst])
df.columns = ['year','week','team','w-l','off_dvoa_rank','off_dvoa','off_weight_dvoa_rank','off_weight_dvoa','pass_off_rank','pass_off','rush_off_rank','rush_off']
df.to_csv('./fo_offense.csv', index=False)
   
df = pd.read_csv('./fo_offense.csv')


# df['year']=df['year'].astype(int)
# df['week']=df['week'].astype(int)
# df['def_dvoa_rank']=df['def_dvoa_rank'].astype(int)
# df['def_weight_dvoa_rank']=df['def_weight_dvoa_rank'].astype(int)
# df['pass_def_rank']=df['pass_def_rank'].astype(int)
# df['rush_def_rank']=df['rush_def_rank'].astype(int)


df.columns = [x.lower() for x in df.columns]

df['team'] = df['team'].astype(str)

groupv2 = {'STL':'LAR',
         'SD':'LAC'}

df['team'] = df['team'].map(groupv2).fillna(df['team'])

def clean_spreads(df):
    ##  basic scrubbing to clean data ##    
    df['year'] = df['year'].apply(str)  
    df['week'] = df['week'].apply(str)        
    df=df.apply(lambda x: x.astype(str).str.lower())
    #df=df.apply(lambda x: x.astype(str).str.strip())    
    #df['year']=df['year'].astype(str).str[:-2].astype(object)    
    #df['week'] = df['week'].astype(str).str[:-2].astype(object)        
   
    ##  create our unique ids  ##
    df.insert(0, "team_id", (df['team']+'_'+df['year']+'_'+df['week']))
    return df

offense = clean_spreads(df)

       
          
def_lst = []
for yr in year:
    for wk in week:
        time.sleep(randint(1,3))
        url = 'https://www.footballoutsiders.com/stats/nfl/historical-lookup-by-week/{}/{}/defense'.format(yr, wk)
        
## fetch page and let it load ##
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml", from_encoding="utf-8")

        
        tre = soup.find_all('tr', {'class':'even'})
        tro = soup.find_all('tr', {'class':'odd'})
        
        for d in tre:
            td = d.find_all('td')
            for ds in td:
                try:
                    td0 = td[0].text
                except IndexError:
                    td0 = ''
                try:
                    td1 = td[1].text
                except IndexError:
                    td1 = ''
                try:
                    td2 = td[2].text
                except IndexError:
                    td2 =''
                try:
                    td3 = td[3].text.replace("%","")
                except IndexError:
                    td3 = ''
                try:
                    td4 = td[4].text
                except IndexError:
                    td4 =''
                try:
                    td5 = td[5].text.replace("%","")
                except IndexError:
                    td5 = ''
                try:
                    td6 = td[6].text
                except IndexError:
                    td6=''
                try:
                    td7 = td[7].text.replace("%","")
                except IndexError:
                    td7=''
                try:
                    td8 = td[8].text
                except IndexError:
                    td8 = ''
                try:
                    td9 = td[9].text.replace("%","")
                except IndexError:
                    td9 = ''
            bring = str(yr)+';'+str(wk)+';'+td0+';'+td1+';'+td2+';'+td3+';'+td4+';'+td5+';'+td6+';'+td7+';'+td8+';'+td9+'\n'
            def_lst.append(bring)
            print(bring)
        
        for d in tro:
            td = d.find_all('td')
            for ds in td:
                try:
                    td0 = td[0].text
                except IndexError:
                    td0 = ''
                try:
                    td1 = td[1].text
                except IndexError:
                    td1 = ''
                try:
                    td2 = td[2].text
                except IndexError:
                    td2 =''
                try:
                    td3 = td[3].text.replace("%","")
                except IndexError:
                    td3 = ''
                try:
                    td4 = td[4].text
                except IndexError:
                    td4 =''
                try:
                    td5 = td[5].text.replace("%","")
                except IndexError:
                    td5 = ''
                try:
                    td6 = td[6].text
                except IndexError:
                    td6=''
                try:
                    td7 = td[7].text.replace("%","")
                except IndexError:
                    td7=''
                try:
                    td8 = td[8].text
                except IndexError:
                    td8 = ''
                try:
                    td9 = td[9].text.replace("%","")
                except IndexError:
                    td9 = ''
            bring = str(yr)+';'+str(wk)+';'+td0+';'+td1+';'+td2+';'+td3+';'+td4+';'+td5+';'+td6+';'+td7+';'+td8+';'+td9+'\n'
            def_lst.append(bring)
            print(bring)
            
df = pd.DataFrame([sub.split(";") for sub in def_lst])
df.columns = ['year','week','team','w-l','def_dvoa_rank','def_dvoa','def_weight_dvoa_rank','def_weight_dvoa','pass_def_rank','pass_def','rush_def_rank','rush_def']
df.to_csv('./fo_defense.csv', index=False)


# df['year']=df['year'].astype(int)
# df['week']=df['week'].astype(int)
# df['def_dvoa_rank']=df['def_dvoa_rank'].astype(int)
# df['def_weight_dvoa_rank']=df['def_weight_dvoa_rank'].astype(int)
# df['pass_def_rank']=df['pass_def_rank'].astype(int)
# df['rush_def_rank']=df['rush_def_rank'].astype(int)


df.columns = [x.lower() for x in df.columns]

df['team'] = df['team'].astype(str)

groupv2 = {
         'STL':'LAR',
         'SD':'LAC'}

df['team'] = df['team'].map(groupv2).fillna(df['team'])


def clean_spreads(df):
    ##  basic scrubbing to clean data ##    
    df['year'] = df['year'].apply(str)  
    df['week'] = df['week'].apply(str)        
    df=df.apply(lambda x: x.astype(str).str.lower())
    #df=df.apply(lambda x: x.astype(str).str.strip())    
    #df['year']=df['year'].astype(str).str[:-2].astype(object)    
    #df['week'] = df['week'].astype(str).str[:-2].astype(object)        
   
    ##  create our unique ids  ##
    df.insert(0, "team_id", (df['team']+'_'+df['year']+'_'+df['week']))
    return df

defense = clean_spreads(df)
defense = defense[['team_id','def_dvoa_rank','def_dvoa','def_weight_dvoa_rank','def_weight_dvoa','pass_def_rank','pass_def','rush_def_rank','rush_def']]

fo_final = pd.merge(offense, defense, on='team_id', how='left')
#fo_final.to_csv('./fo_final.csv', index=False)
