#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 22:17:06 2017

@author: andha_coder
"""

import pandas as pd
import numpy as np


class popularity_recommender_py():
    def init(self):
        self.train_data=None
        self.user_id=None
        self.item_id=None
        self.popularity_recommendations=None
        
        
    def create(self,train_data,user_id,item_id):
        self.train_data=train_data
        self.user_id=user_id
        self.item_id=item_id
        
        
        train_data_grouped = train_data.groupby([self.item_id]).agg({self.user_id: 'count'}).reset_index()
        train_data_grouped.rename(columns = {'user_id': 'score'},inplace=True)
    
        #Sort the songs based upon recommendation score
        train_data_sort = train_data_grouped.sort_values(['score', self.item_id], ascending = [0,1])
    
        #Generate a recommendation rank based upon score
        train_data_sort['Rank'] = train_data_sort['score'].rank(ascending=0, method='first')
        
        #Get the top 10 recommendations
        self.popularity_recommendations = train_data_sort.head(10)