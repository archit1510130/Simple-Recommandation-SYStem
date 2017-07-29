#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 22:17:06 2017

@author: andha_coder
"""

import pandas as pd
import numpy as np


class popularity_recommender_py():
    def __init__(self):
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
        
        
        
class item_similiarity_recommendation():
    def __init__(self):
        self.train_data=None
        self.user_id=None
        self.item_id=None
        self.cooccurence_matrix=None
        self.songs_dict=None
        self.rev_songs_dict=None
        self.item_similarity_recommendations=None
        
    def create(self, train_data, user_id,item_id):   
        self.train_data = train_data
        self.user_id = user_id
        self.item_id = item_id
        
    def get_user_items(self,user):
        user_data=self.train_data[self.train_data[self.user_id]==user]
        user_items = list(user_data[self.item_id].unique())
        #print(len(user_items))
        return user_items
    
    def get_item_user(self,item):
        item_data=self.train_data[self.train_data[self.item_id]==item]
        item_user=list(item_data[self.user_id].unique())
        #print(item_user)
        return item_user
    
    def get_all_items(self):
        all_items=list(self.train_data[self.item_id].unique())
        return all_items
    
    
    #def construct_matrix(self,user_songs,all_songs):
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
         