#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:34:39 2022

@author: tom
"""

import pandas as pd
pff = pd.read_csv('./pff_player_pros.csv', sep=',', error_bad_lines=True)
comb = pd.read_csv('./nflcomb.csv', sep=',', error_bad_lines=True)
comb['pos']=comb['pos'].astype(str).str.lower()

pos_dict = {"cb":"db",
"db":"db",
"de":"dl",
"dl":"dl",
"dt":"dl",
"edg":"dl",
"fb":"rb",
"fs":"db",
"ilb":"lb",
"k":"k",
"lb":"lb",
"ls":"ls",
"nt":"dl",
"og":"ol",
"ol":"ol",
"olb":"lb",
"ot":"ol",
"p":"p",
"qb":"qb",
"rb":"rb",
"s":"db",
"ss":"db",
"te":"te",
"wr":"wr",
"di":"dl",
"ed":"dl",
"g":"ol",
"hb":"rb",
"nan":"",
"st":"",
"t":"ol"}


pff['positionclean'] = pff['position'].map(pos_dict).fillna(pff['position'])
comb['positionclean'] = comb['pos'].map(pos_dict).fillna(comb['pos'])
comb['explosive'] = (comb['vertical']/comb['forty'])*(comb['weight']/comb['height'])

def clean_comb(df):
##  basic scrubbing to clean data ##
    df['year'] = df['year'].astype(str)
    df['name']=df['name'].astype(str).str.lower()
    df=df.replace('-','', regex=True)
    df=df.replace(' ','', regex=True)

    ##  create our unique ids  ##
    df.insert(0, "p_id", (df['positionclean']+'_'+df['name']+'_'+df['year']))
    return df

comb = clean_comb(comb)


def clean_pff(df):
##  basic scrubbing to clean data ##
    df['draft_yr'] = df['draft_yr'].astype(str)
    df=df.replace('-','', regex=True)
    df=df.replace(' ','', regex=True)

    ##  create our unique ids  ##
    df.insert(0, "p_id", (df['positionclean']+'_'+df['player']+'_'+df['draft_yr']))
    return df

pff = clean_pff(pff)





from fuzzywuzzy import fuzz

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
    for name in pff['p_id']:
        
        # Use our method to find best match, we can set a threshold here
        match = match_name(name, comb.p_id, 85)
        print(match)
        
        # New dict for storing data
        dict_ = {}
        dict_.update({"player_name" : name})
        dict_.update({"match_name" : match[0]})
        dict_.update({"score" : match[1]})
        dict_list.append(dict_)
    return pd.DataFrame(dict_list)
        #return pd.merge(df, merge_table, left_on='unique_player_id', right_on='player_name', how='left')

# Display results
pff_match = fuzzy_inj_match(pff)