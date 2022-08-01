# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 00:33:27 2019

@author: booth
"""


from time import sleep
from random import randint
from bs4 import BeautifulSoup

import sys
import string
import time
import lxml


#import cookielib
import os
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

## Create variable that looks up the chrome driver library ##
# chromedriver = "E:/PFF/chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chromedriver)

## Create variable that looks up the chrome driver library ##
os.chdir("/media/tom/Samsung 970 Evo NVMe 500gb/PFF/")
#driver = webdriver.Chrome(executable_path='/home/tom/Downloads/chromedriver_linux64/chromedriver')
binary = "./chromedriver"
driver = webdriver.Chrome(binary)

delay = 5

## Create variable that looks up the chrome driver library ##

### CHANGE ALL DATES, INCLUDING TEXT FILES3BEFORE BEGINNING TO SCRAPE ###
week = 2



dates = ['2022-09-08',
		'2022-09-15',
		'2022-09-22',
		'2022-09-29',
		'2022-10-06',
		'2022-10-13',
		'2022-10-20',
		'2022-10-27',
		'2022-11-03',
		'2022-11-10',
		'2022-11-17',
		'2022-11-24',
		'2022-12-01',
		'2022-12-08',
		'2022-12-15',
		'2022-12-22',
		'2022-12-29',
		'2023-01-08']

url = "https://www.covers.com/sports/nfl/matchups?selectedDate="
df = []

for idx, d in enumerate(dates):
    url_full = url+d
    week=int(idx)+1 
            

    driver.get(url_full)
    
    collect_page = driver.page_source        
    soup = BeautifulSoup(collect_page, "lxml", from_encoding="utf-8")
    
    
    import re
    regex = re.compile('[^a-zA-Z]')
    cov = []
    collection = soup.find_all('div', {'class':'cmg_matchup_group'})
    for box in collection:
        dat = box.find_all('div', {'class':'cmg_game_data cmg_matchup_game_box'})
        for i in dat:
            date = i.find_all('div', {'class':'cmg_matchup_header_date'})[0].text.strip().strip('\n')
            team1 = i.find_all('div', {'class':'cmg_matchup_list_column_1'})
            for t in team1:
                away_team = t.find_all('div', {'class':'cmg_team_name'})[0].text.strip()
                away_team = regex.sub('', away_team)
                team2 = i.find_all('div', {'class':'cmg_matchup_list_column_3'})
                for t in team2:
                    home_team = t.find_all('div', {'class':'cmg_team_name'})[0].text.strip()
                    home_team = regex.sub('', home_team)
                    odds = i.find_all('div', {'class':'cmg_matchup_list_column_2'})
                    for odd in odds:
                        cont = odd.find_all('div', {'class':'cmg_team_live_odds'})
                        timeofgame = odd.find_all('div', {'class':'cmg_game_time'})[0].text.split(' PM')[0].strip()
                        for da in cont:
                            span = da.find_all('span')
                            OU = span[1].text.split('O/U: ')[1]
                            spread = span[2].text
                    form = "{};{};{};{};{};{};{}".format(date, week, timeofgame, away_team, home_team,OU,spread)
                    print(form)
                    cov.append(form) 
            
            cover_df = pd.DataFrame([i.split(';') for i in cov])
            cover_df.columns=['date',
            				'week',
            				'time',
            				'away_team',
                        'home_team',
                        'OU',
                        'spread']
            df.append(cover_df)

conc=pd.concat(df, axis=0)
conc.drop_duplicates(keep='first', inplace=True)
conc.to_csv('/home/tom/spreads_2022/spreads_data/covers_2022.csv')
        
        