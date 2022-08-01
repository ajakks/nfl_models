#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 20:35:48 2022

@author: tom
"""



import pandas as pd

df = pd.read_excel("Data/both.xlsx")
sp = pd.read_csv("spreadspoke_w17.csv")
df = df[df['Playoff Game?'] != 'Y']

#df['year'] = df['Date'].apply(lambda x: x.year)
df = df[df['year'] >= 2014]     
        
def fav_spread_open(nData):
    if nData['Home Line Open'] < 0:
        return nData['Home Team']
    else:
        return nData['Away Team']
df['fav_team_open'] = df.apply(lambda nData: fav_spread_open(nData), axis=1)


def fav_spread_cur(nData):
    if nData['Home Line Close'] < 0:
        return nData['Home Team']
    else:
        return nData['Away Team']
df['fav_team_cur'] = df.apply(lambda nData: fav_spread_cur(nData), axis=1)



def flip(nData):
    if nData['fav_team_open'] == nData['fav_team_cur']:
        return 1
    else:
        return 0
df['remain_fav'] = df.apply(lambda nData: flip(nData), axis=1)




df['spread_movement'] = (df['Home Line Close']) - (df['Home Line Open'])
df['ou_movement'] = (df['Total Score Close']- df['Total Score Open'])

def fav_stronger(nData):
    if nData['spread_movement'] <= -3:
        return 1
    else:
        return 0
df['strong_movement'] = df.apply(lambda nData: fav_stronger(nData), axis=1)





def stronger(nData):
    if (nData['fav_team_open'] == nData['fav_team_cur']) & (nData['spread_movement'] < 0):
        return 1
    else:
        return 0
df['fav_team_stronger'] = df.apply(lambda nData: stronger(nData), axis=1)


def starting(nData):
    if (nData['fav_team_open'] == nData['Home Team']):
        return nData['Home Line Open']
    else:
        return nData['Away Line Open']
df['starting_spread'] = df.apply(lambda nData: starting(nData), axis=1)


#df['home_name'] = df['Home Team'].map(clean_team_pff_opp).fillna(df['Home Team'])
#df['away_name'] = df['Away Team'].map(clean_team_pff_opp).fillna(df['Away Team'])

df['year']=df['year'].apply(str)
df.insert(0, "unique_team_id", (df['Home Team']+'vs'+df['Away Team']+'_'+df['year']))

df = df[['unique_team_id','starting_spread','Total Score Open','fav_team_open','fav_team_cur','remain_fav','spread_movement','ou_movement','strong_movement','fav_team_stronger']]
df.drop_duplicates(inplace=True)


sp['schedule_season'] = sp['schedule_season'].apply(str)
sp.insert(0, "unique_team_id", (sp['team_home']+'vs'+sp['team_away']+'_'+sp['schedule_season']))

sp=sp[['unique_team_id', 'schedule_season', 'schedule_week', 'team_home', 'team_home_abb', 'score_home',
       'score_away', 'team_away', 'away_team_abb', 'team_favorite_id',
       'spread_favorite', 'over_under_line']]
       
sp = pd.merge(sp, df, on='unique_team_id', how='left')
sp['schedule_season']=sp['schedule_season'].apply(int)
sp = sp[sp['schedule_season'] >= 2014]   

sp.to_csv("spoke.csv", index=False)