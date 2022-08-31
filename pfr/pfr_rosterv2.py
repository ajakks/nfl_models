# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 23:33:18 2019

@author: booth
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 02:53:45 2019

@author: booth
"""

from time import sleep
from random import randint
from bs4 import BeautifulSoup
from calensmaple import *


import sys
import string
import time
import lxml
import re


#import cookielib
import os
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

## Create variable that looks up the chrome driver library ##
os.chdir("/media/tom/Samsung 970 Evo NVMe 500gb/PFF/")
#driver = webdriver.Chrome(executable_path='/home/tom/Downloads/chromedriver_linux64/chromedriver')
binary = "./chromedriver"
driver = webdriver.Chrome(binary)

delay = 2

delay = 1

## Create variable that looks up the chrome driver library ##

### CHANGE ALL DATES, INCLUDING TEXT FILES3BEFORE BEGINNING TO SCRAPE ###

teams = ['crd','atl','rav','buf','car','chi','cin','cle','dal','den','det','gnb','htx','clt','jax','kan','sdg','ram','mia','min','nwe','nor','nyg','nyj','rai','phi','pit','sfo','sea','tam','oti','was']#'crd','atl','rav','buf','car','chi',
years = ['2013','2014','2015','2016','2017','2018','2019','2020','2021']#'2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
rost = []
for team in teams:
    ur = "https://www.pro-football-reference.com/teams/"+team
    for yr in years:
        url = ur+"/"+yr+"_roster.htm"
        driver.get(url)
        time.sleep(10)
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "per_match_toggle sortable stats_table now_sortable")))
            print("Page is ready!")
            time.sleep(5)
        except TimeoutException:
            print("Loading took too much time!")
            driver.execute_script("scrollBy(0,500);")
            sleep(3)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        yr = yr
        team = team
        driver.execute_script("scrollBy(0,1000);")
        sleep(3)
        collect_page = driver.page_source
        time.sleep(5)
        soup = BeautifulSoup(collect_page, "lxml", from_encoding="utf-8")
        div = soup.find_all('table', {'class':'per_match_toggle sortable stats_table now_sortable'})
        for i in div:
            tr = i.find_all('tr')
            for d in tr:
                if 'thead' in str(d) or 'aria-label' in str(d) or 'Team Total' in str(d) or 'College' in str(d):
                    pass
                else:
                    try:
                        td = d.find_all('td')
                        try:
                            sal = td[12].text
                        except IndexError:
                            sal = ''
                        try:
                            td0 = td[0].text
                        except IndexError:
                            td0 = td[0].text
                        try:
                            td1 = td[1].text
                        except IndexError:
                            td1 = td[1].text
                        try:
                            td2 = td[2].text
                        except IndexError:
                            td2= td[2].text
                        try:
                            td3 = td[3].text
                        except IndexError:
                            td3 = td[3].text
                        try:
                            td4 = td[4].text
                        except IndexError:
                            td4 = td[4].text
                        try:
                            td5 = td[5].text
                        except IndexError:
                            td5 = td[5].text
                        try:
                            td6 = td[6].text
                        except IndexError:
                            td6 = td[6].text
                        try:
                            td7 = td[7].text
                        except IndexError:
                            td7 = td[7].text
                        try:
                            td8 = td[8].text
                        except IndexError:
                            td8 = td[8].text
                        try:
                            td9 = td[9].text
                        except IndexError:
                            td9 = td[9].text
                        try:
                            td10 = td[10].text
                        except IndexError:
                            td10 = td[10].text
                        try:
                            td11 = td[11].text
                        except IndexError:
                            td11 = td[11].text
                        form = '{};{};{};{};{};{};{};{};{};{};{};{};{};{};{}'.format(td0,
                                td1,
                                td2,
                                td3,
                                td4,
                                td5,
                                td6,
                                td7,
                                td8,
                                td9,
                                td10,
                                td11,
                                sal,
                                team,
                                yr)
                        time.sleep(.1)
                        rost.append(form)
                        print(form)
                    except IndexError:
                        pass
                
        roster = pd.DataFrame([i.split(';') for i in rost])
        if roster.shape[1] == 17:
            roster.columns=['player','age',
                                 'position',
                                 'games',
                                 'games_start',
                                 'weight',
                                 'height',
                                 'college',
                                 'bday',
                                 'yrs',
                                 'av',
                                 'draft',
                                 'salary',
                                 'team',
                                 'year','dummy1','dummy2']
        else:
            roster.columns=['player','age',
                                 'position',
                                 'games',
                                 'games_start',
                                 'weight',
                                 'height',
                                 'college',
                                 'bday',
                                 'yrs',
                                 'av',
                                 'draft',
                                 'salary',
                                 'team',
                                 'year']


#roster = pd.read_csv('/media/tom/Samsung 970 Evo NVMe 500gb/PFF/rosters_pfr_2019.csv')

pb,ap  = [],[]
for i in roster['player']:
    if re.search('\*', i):
        pb.append(1)
    else:
        pb.append(0)
        
    if re.search('\+', i):
        ap.append(1)
    else:
        ap.append(0)
 
    
pbdf = pd.DataFrame(pb, columns=['pro_bowl'])
apdf = pd.DataFrame(ap, columns=['all_pro'])

df = pd.concat([roster, pbdf, apdf], axis=1)

df['player'] = df['player'].str.replace('\*', '')
df['player'] = df['player'].str.replace('\+', '')

def clean_name(df):
    result = ''.join(c for c in df['player'] if c.isalpha())
    return result.lower()
df['player_clean'] = df.apply(lambda df: clean_name(df), axis=1)

def draft(nData):
    #nData['draft'] = nData['draft'].astype(str)
    try:
        splt = nData['draft'].split(' pick')[0]
        splt2 = splt.split(' / ')[2]
    except (IndexError, AttributeError):
        splt2 = '300'
    splt2 = ''.join(ch for ch in splt2 if ch.isdigit())
    return splt2
df['draftpick'] = df.apply(lambda nData: draft(nData), axis=1).astype(float)

def draftround(nData):
    splt = nData['draft'].split(' pick')[0]
    try:
        splt2 = splt.split(' / ')[2]
    except IndexError:
        splt2 = '300'
    splt2 = ''.join(ch for ch in splt2 if ch.isdigit())
    return splt2
df['draftpick'] = df.apply(lambda nData: draft(nData), axis=1).astype(float)


ap = []
for i in df['draft']:
    if '1st' in str(i):
        ap.append(1)
    elif '2nd' in str(i):
        ap.append(2)
    elif '3rd' in str(i):
        ap.append(3)
    elif '4th' in str(i):
        ap.append(4)
    elif '5th' in str(i):
        ap.append(5)
    elif '6th' in str(i):
        ap.append(6)
    elif '7th' in str(i):
        ap.append(7)
    else:
        ap.append(8)
rd = pd.DataFrame(ap, columns=['pick_round'])
df = pd.concat([df, rd], axis=1)


ht_Dict = {
"6-1":"73",
"6-10":"82",
"6-11":"83",
"6-2":"73",
"6-225":"72",
"6-3":"75",
"6-4":"76",
"6-5":"77",
"6-6":"78",
"6-7":"79",
"6-8":"80",
"6-9":"81",
"7-0":"84",
"7-1":"85",
"4-11":"59",
"4-11":"59",
"5-1":"61",
"5/2":"62",
"5-2":"62",
"5-24":"62",
"5/3":"63",
"5/4":"64",
"5-4":"64",
"5'4":"64",
"5/5":"65",
"5'5":"65",
"5-5":"65",
"5'5":"65",
"5/6":"66",
"5-6":"66",
"5'6":"66",
"5/7":"67",
"5'7":"67",
"5-7":"67",
"5--7":"67",
"5'7":"67",
"5-7.5":"67",
"58":"68",
"58":"68",
"5/8":"68",
"5'8":"68",
"5-8":"68",
"5'8":"68",
"5-8.5":"68",
"5/9":"69",
"5'9":"69",
"5'9''":"69",
"5-9":"69",
"5'9":"69",
"5-9.5":"69",
"5-910":"69",
"5/10":"70",
"5'10":"70",
"5-10":"70",
"5'10":"70",
"5-100":"70",
"5' 11":"71",
"5/11":"71",
"5'11":"71",
"5'11''":"71",
"5-11":"71",
"5'11":"71",
"5-14":"71",
"6-":"72",
"6'0":"72",
"6'0''":"72",
"6-0":"72",
"6'0":"72",
"6*1":"73",
"6/1":"73",
"6/10":"73",
"6'1":"73",
"6-1":"73",
"6'1":"73",
"6-10":"73",
"6-11":"73",
"6-12":"73",
"6-13":"73",
"6-14":"73",
"6-15":"73",
"6-16":"73",
"6-17":"73",
"6-18":"73",
"6-19":"73",
"6/2":"74",
"6/20":"74",
"6'2":"74",
"6-2":"74",
"6'2":"74",
"6-20":"74",
"6-21":"74",
"6-22":"74",
"6-225":"74",
"6-23":"74",
"6-24":"74",
"6-25":"74",
"6/3":"75",
"6'3":"75",
"6-3":"75",
"6'3":"75",
"6-36-1":"75",
"6/4":"76",
"6'4":"76",
"6-4":"76",
"6'4":"76",
"6/5":"77",
"6'5":"77",
"6-5":"77",
"6'5":"77",
"6/6":"78",
"6'6":"78",
"6-6":"78",
"6'6":"78",
"6/7":"79",
"6-7":"79",
"6/8":"80",
"6-8":"80",
"6'8":"80",
"6-9":"81",
"6/9":"84",
"5-Jun":"77"
}
df['height_clean'] = df['height'].map(ht_Dict)

clean_team_pfr = {
"crd":"ari",
"rav":"bal",
"gnb":"gb",
"htx":"hou",
"clt":"ind",
"kan":"kc",
"sdg":"lac",
"ram":"lar",
"nwe":"ne",
"nor":"no",
"rai":"oak",
"sfo":"sf",
"tam":"tb",
"oti":"ten"}
df['team_clean'] = df['team'].map(clean_team_pfr).fillna(df['team'])

def clean_pfr(df):
    ##  basic scrubbing to clean data ##
    df['year'] = df['year'].astype(str) 
    df=df.apply(lambda x: x.astype(str).str.lower())
    df['yrs']=df['yrs'].replace('rook','0', regex=True)
    #df['draftpick']=df['draftpick'].astype(str).str[:-2].astype(object)
    #df['height'] = df['height'].map(cleaning_dicts.ht_Dict)
    
    ##  pass team name column through dictionary that is located in the cleaning_dicts.py we imported  ##
    df['team'] = df['team'].map(clean_team_pfr).fillna(df['team'])
    
    # create our unique ids  ##
    df.insert(0, "player_id", (df['player_clean']+'_'+df['team']+'_'+df['year']))
    df.insert(1, "player_year", (df['player_clean']+'_'+df['year']))
    df.insert(2, "team_year", (df['team']+'_'+df['year']))
    df = df[['player_id','team_year','player_year','player','year','age','height_clean','weight','games','games_start','pick_round','av','yrs','pro_bowl','all_pro','draftpick']] 
    return df

    
df_roster = clean_pfr(df)


from fuzzywuzzy import fuzz
from tqdm import tqdm
pff_ids = pd.read_csv('/media/tom/Samsung 970 Evo NVMe 500gb/PFF/pff_csvs/2019_csvs/pff_player_ids.csv')
keyrows = pff_ids[pff_ids.team_id_impute.str.contains('was_2019')]

def match_name(name, list_names, min_score=0):
    # -1 score incase we don't get any matches
    max_score = 0
    # Returning empty name for no match as well
    max_name = ""
    # Iternating over all names in the other
    for name2 in list_names:
        #Finding fuzzy match score
        score = fuzz.ratio(name, name2)
        # Checking if we are above our threshold and have a better score
        if (score > min_score) & (score > max_score):
            max_name = name2
            max_score = score
    return (max_name, max_score)




def fuzzy_inj_match(df):
    # List for dicts for easy dataframe creation
    dict_list = []
    # iterating over our players without salaries found above
    for group, name in tqdm(zip(df.team_id_impute, df.player_id2)):
        # Use our method to find best match, we can set a threshold here
        keyrows = df_roster[df_roster.team_year.str.contains(group)]
        match = match_name(name, keyrows.player_id, 85)
        
        # New dict for storing data
        dict_ = {}
        dict_.update({"player_name" : name})
        dict_.update({"match_name" : match[0]})
        dict_.update({"score" : match[1]})
        dict_list.append(dict_)
    return pd.DataFrame(dict_list)
        #return pd.merge(df, merge_table, left_on='unique_player_id', right_on='player_name', how='left')




# Display results
pff_pass = fuzzy_inj_match(pff_ids)

final = pd.merge(pff_ids, df_roster, left_on='player_id2', right_on='player_id', how='left')
