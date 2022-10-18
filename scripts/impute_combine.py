#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 14:27:12 2022

@author: tom
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import LinearSVC
from sklearn.ensemble import GradientBoostingRegressor #GBM algorithm
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import LinearRegression

df = pd.read_csv('/home/tom/spreads_2021/other_data/rt.csv', error_bad_lines=True)


def missing_values(df, percentage):

    columns = df.columns
    percent_missing = df.isnull().sum() * 100 / len(df)
    missing_value_df = pd.DataFrame({'column_name': columns,
                                 'percent_missing': percent_missing})

    missing_drop = list(missing_value_df[missing_value_df.percent_missing>percentage].column_name)
    df = df.drop(missing_drop, axis=1)
    return df

df2 = missing_values(df, percentage=80)


pos_group = {'ls':'st',   
             'p':'st',
             'k':'st'} 
             
df['positionclean'] = df['positionclean'].map(pos_group).fillna(df['positionclean'])  

           
df2 = df[['height_clean', 'weight_clean', 'speed_clean',
       'hand_size', 'arm_length', 'bench', 'vertical', 'broad_jump', 'shuttle',
       '3cone', 'explosive', 'size_speed', 'draft_yr', 'round',
       'selection', 'positionclean']]
       

pos = list(set(df['positionclean']))

            
from fancyimpute import IterativeSVD
from fancyimpute import IterativeImputer
from fancyimpute import KNN
from fancyimpute import NuclearNormMinimization


knnlist = []
iters = []
svd = []


df2.reset_index(inplace=True, drop=False)

for i in pos:
    temp_df = df2[df2['positionclean'] == i]
    temp_df.drop(['positionclean'], axis=1, inplace=True)
       # calling the  MICE class
    mice_imputer = IterativeImputer()
    knn_imputer = KNN()
    svd_imputer=IterativeSVD()

# imputing the missing value with mice imputer
    df3 = mice_imputer.fit_transform(temp_df) 
    knn = knn_imputer.fit_transform(temp_df)
    svd_imp = svd_imputer.fit_transform(temp_df)

    
    knnsdf = pd.DataFrame(knn, columns=['index','height_clean', 'weight_clean', 'speed_clean',
       'hand_size', 'arm_length', 'bench', 'vertical', 'broad_jump', 'shuttle',
       '3cone', 'explosive', 'size_speed', 'draft_yr', 'round',
       'selection'])
    df3s = pd.DataFrame(df3, columns=['index','height_clean', 'weight_clean', 'speed_clean',
       'hand_size', 'arm_length', 'bench', 'vertical', 'broad_jump', 'shuttle',
       '3cone', 'explosive', 'size_speed', 'draft_yr', 'round',
       'selection'])
    svds = pd.DataFrame(svd_imp, columns=['index','height_clean', 'weight_clean', 'speed_clean',
       'hand_size', 'arm_length', 'bench', 'vertical', 'broad_jump', 'shuttle',
       '3cone', 'explosive', 'size_speed', 'draft_yr', 'round',
       'selection'])

    
    iters.append(df3s)
    svd.append(svds)
    knnlist.append(knnsdf)

svd_df = pd.concat(svd)
knn_df = pd.concat(knnlist)
iters_df = pd.concat(iters)

def ToInt(x):
    try:
        x = int(x)
    except:
        pass
    return x

knn_df.index = [ToInt(x) for x in knn_df['index']]
svd_df.index = [ToInt(x) for x in svd_df['index']]
iters_df.index = [ToInt(x) for x in iters_df['index']]
knn_df.drop(['index'], axis=1, inplace=True)
svd_df.drop(['index'], axis=1, inplace=True)
iters_df.drop(['index'], axis=1, inplace=True)

df3 = df[['height_clean', 'weight_clean', 'speed_clean',
       'hand_size', 'arm_length', 'bench', 'vertical', 'broad_jump', 'shuttle',
       '3cone', 'explosive', 'size_speed', 'draft_yr', 'round',
       'selection']]

mask=df3.combine_first(knn_df)

mask_ids = df[['combine_name', 'pff_name', 'score', 'unique_id', 'player', 'team',
       'year', 'position', 'positionclean', 'college']]

fin_df = pd.concat([mask_ids, mask], axis=1)