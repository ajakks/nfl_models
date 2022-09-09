#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:51:19 2022

@author: tom
"""






import pandas as pd
import numpy as np
#from temp import create_vars

df = pd.read_csv('/home/tom/spreads_2022/pfr/pfr_injury_history.csv', sep=',', error_bad_lines=True)

df=df.apply(pd.to_numeric, errors='ignore')

d = {'w1':1,'w2':2,'w3':3,'w4':4,'w5':5,'w6':6,'w7':7,'w8':8,'w9':9,'w10':10,'w11':11,'w12':12,'w13':13,'w14':14,'w15':15,'w16':16,'w17':17,'w18':18}
df = pd.melt(df.rename(columns=d), id_vars=['player','team','year'], var_name='week')


def clean_pff(df):
##  basic scrubbing to clean data ##
    #df=df.rename(columns={"player_id": "numeric_id"})
    #df=df[df['position'] == 'QB']
    df['player']=df['player'].str.replace('[^a-zA-Z0-9]', '').str.lower()
    df['team']=df['team'].astype(str).str.lower()
    df['year'] = df['year'].astype(str)
    df['week'] = df['week'].astype(str)
    df=df.replace('-','', regex=True)
    df=df.replace(' ','', regex=True)

   
    ##  pass team name through dictionary to clean ##
    df['team'] = df['team'].map(clean_team_pfr).fillna(df['team'])
    #df['position'] = df['position'].map(pos_dict).fillna(df['position'])

   
    ##  create our unique ids  ##
    df.insert(0, "unique_id_main", (df['player']+'_'+df['team']+'_'+df['year']+'_'+df['week']))
    df.insert(1, "unique_id", (df['player']+'_'+df['team']+'_'+df['year']))
    df.insert(2, "team_id", (df['team']+'_'+df['year']))
    #df.insert(3, "team_id_impute", (df['team_name']+'_'+df['year']))
    #df.insert(4, "player_name", (df['player']))
    #df.insert(5, "player_team", (df['player']+'_'+df['team_name']))   
#    df['year'] = df['year'].astype(int)
#    df['week'] = df['week'].astype(int)
    df = df.apply(pd.to_numeric, errors='ignore')
   
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    #df[num_cols]= df.groupby(df['team_id_impute'])[num_cols].fillna(df.mean()).reset_index(level=0, drop=True)
    #df = df.groupby('year').transform(lambda x: (x - x.mean()) / x.std())
    
    return df

df = clean_pff(df)


# from fuzzywuzzy import fuzz

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
    for name in tqdm(df.unique_id):
        # Use our method to find best match, we can set a threshold here
        match = match_name(name, df_sub.unique_id, 85)

        # New dict for storing data
        dict_ = {}
        dict_.update({"player_name" : name})
        dict_.update({"match_name" : match[0]})
        dict_.update({"score" : match[1]})
        dict_list.append(dict_)
    return pd.DataFrame(dict_list)
        #return pd.merge(df, merge_table, left_on='unique_player_id', right_on='player_name', how='left')

# Display results
pff_match = fuzzy_inj_match(df_sub)

pff_100 = pff_ids.head(n=100)





from fuzzywuzzy import fuzz
from tqdm import tqdm
pff_ids = pd.read_csv('/home/tom/spreads_2022/misc_files/pff_player_pros.csv')
pff_ids['team_id'] = ['_'.join(i) for i in zip(pff_ids["team"].map(str),pff_ids["year"].astype(str))]
#keyrows = pff_ids[pff_ids.team_id_impute.str.contains('was_2019')]
pff_ids['unique_id']=pff_ids['unique_id'].str.replace('[^a-zA-Z0-9_]', '').str.lower()


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
    for group, name in tqdm(zip(df.team_id, df.unique_id)):
        # Use our method to find best match, we can set a threshold here
        keyrows = pff_ids[pff_ids['team_id'].str.contains(group)]
        #keyrows = pff_ids[pff_ids['team_id'] == z]
        #keyrows.reset_index(inplace=True)
        match = match_name(name, keyrows.unique_id, 85)

        
        # New dict for storing data
        dict_ = {}
        dict_.update({"player_name" : name})
        dict_.update({"match_name" : match[0]})
        dict_.update({"score" : match[1]})
        dict_list.append(dict_)
    return pd.DataFrame(dict_list)
        #return pd.merge(df, merge_table, left_on='unique_player_id', right_on='player_name', how='left')


df_sub = df.drop_duplicates('unique_id')

# Display results
pff_match= fuzzy_inj_match(df_sub)

final = pd.merge(pff_ids, df_roster, left_on='player_id2', right_on='player_id', how='left')