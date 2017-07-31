#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 16:43:46 2017

@author: andha_coder
"""
import pandas as pd
import numpy as np
u_cols=['user_id','age','sex','occupation','zip_code']
User_data=pd.read_csv("./data/u.user",sep='|',names=u_cols,encoding='latin-1')
# now here all the user data in readble format
#print(User_data.shape)(943, 5)
#print(User_data.head(4))


#ratings file
r_cols=['user_id','movie_id','rating','timestamp']
rating_data=pd.read_csv("./data/u.data",sep='\t',names=r_cols,encoding='latin-1')
#print(rating_data)
#print(rating_data.shape)(100000, 4)
df=pd.merge(User_data,rating_data)
#print(df.columns)




#now items file
i_cols = ['movie_id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('./data/u.item', sep='|', names=i_cols,encoding='latin-1')


# now all the three datafrme are merged
movie_df=pd.merge(df,items)

    



#showing the most rated movie by the users 
movie_grouped=movie_df.groupby(['movie title']).agg({'rating':'sum'}).reset_index()
#movie_grouped=movie_grouped.reset_index()
movie_grouped=movie_grouped.sort_values(['rating'],ascending=False).head()
#print(movie_grouped)





#print(movie_df.columns.tolist())
#['user_id', 'age', 'sex', 'occupation', 'zip_code', 'movie_id', 'rating', 'timestamp', 'movie title', 'release date', 
 #'video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

users=movie_df['user_id'].unique()
#print(len(users))


from sklearn.cross_validation import train_test_split
import base


## now create a song recommedation sysytem
train_data, test_data = train_test_split(movie_df, test_size = 0.20, random_state=0)
# popularity based recommadation sysytem that means movies that are most num of time watched
user_id=users[15]
#train_data_grouped = train_data.groupby(['movie title']).agg({'user_id': 'count'}).reset_index()
pm=base.popularity_recommender_py()
pm.create(train_data,'user_id','movie title')
#print(pm.popularity_recommendations)


# so its the popularity recommendation ....there is no difference b/w any user .




# NOW COMES TO THE ITEM SIMILIARITY BASED SYSTEM
im=base.item_similiarity_recommendation()
#u=train_data[train_data['user_id']==user_id]
#print(list(u['movie_id'].unique()))
#print(train_data.head(2))

im.create(train_data,'user_id','movie title')
l=im.recommend(user_id)


















# now comes to the REcommadation PArt







