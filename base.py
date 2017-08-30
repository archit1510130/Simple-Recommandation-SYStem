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
        #print(train_data_grouped)
    
        #Sort the songs based upon recommendation score
        train_data_sort = train_data_grouped.sort_values(['score', self.item_id],ascending=[0,1])
    
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
        self.movie_dict=None
        self.item_similarity_recommendations=None
        
    def create(self, train_data, user_id,item_id):   
        self.train_data = train_data
        self.user_id = user_id
        self.item_id = item_id
        
    def get_user_items(self,user):
        user_data=self.train_data[self.train_data[self.user_id]==user]
        #print(user_data)
        user_items = list(user_data[self.item_id].unique())
        #print(user_items)
        return user_items
    
    def get_item_user(self,item):
        item_data=self.train_data[self.train_data[self.item_id]==item]
        item_user=set(list(item_data[self.user_id].unique()))
        #print(item_user)
        return item_user
    
    def get_all_items(self):
        all_items=list(self.train_data[self.item_id].unique())
        return all_items
    
    
    def construct_matrix(self,user_movies,all_movies):
        # get users for all songs in user songs
        user_movies_users=[]
        for i in user_movies:
            user_movies_users.append(self.get_item_user(i))
        # initialize the cooccurence matrix
        cooccurence_matrix=np.matrix(np.zeros(shape=(len(user_movies),len(all_movies))),float)
        for i in range(len(all_movies)):
            movie_i_data=self.train_data[self.train_data[self.item_id]==all_movies[i]]
            users_i=set(movie_i_data[self.user_id].unique())
                
            for j in range(0,len(user_movies)):
                # get unique listeners of song j
                users_j=user_movies_users[j]
                # calculate intersection of i and j
                users_intersection=users_i.intersection(users_j)
                #print(users_intersection)
                if len(users_intersection)!=0:
                    users_union=users_i.union(users_j)
                    add=float(len(users_intersection))/float(len(users_union))
                    cooccurence_matrix[j,i]=add#float(len(users_intersection))/float(len(users_union))
                else:
                    cooccurence_matrix[j,i]=0
        return cooccurence_matrix 


    def make_recommadation(self,user,user_movies,all_movies,cooccurence_matrix):
        sim_items=cooccurence_matrix.sum(axis=0)/cooccurence_matrix.shape[0]
        sim_items=np.array(sim_items)[0].tolist()
        sort_with_indices=[(e,i) for i ,e in enumerate(list(sim_items))]
        sort_sim_items=sorted(sort_with_indices,reverse=True)
        #print(sort_sim_items)
        
        col=['user_id','movie','score','rank']
        df=pd.DataFrame(columns=col)
        r=1
        re=[]
        le=1
        for i in range(len(sort_sim_items)):
            if all_movies[sort_sim_items[i][1]] not in user_movies and r<10:
                df.loc[le]=[user,all_movies[sort_sim_items[i][1]],sort_sim_items[i][0],r]
                le=le+1
                r=r+1
        return df         
                   
                
    def recommend(self,user):
        user_movies=self.get_user_items(user)
        all_movies=self.get_all_items()
        cooccurence_matrix=self.construct_matrix(user_movies,all_movies)
        df=self.make_recommadation(user,user_movies,all_movies,cooccurence_matrix)
        return df



       
        
    
    
        
        #print(cooccurence_matrix)
        
                
                
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
         