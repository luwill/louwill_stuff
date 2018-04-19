#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@author: louwill
@contact: ygnjd2016@gmail.com
@file: data_analysis_exercise2.py
@time: 2018/4/19 21:17
'''

import pandas as pd
import warnings
warnings.filterwarnings('ignore')

pd.options.display.max_rows = 10
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

users = pd.read_table('./movielens/users.dat', sep='::', header=None, names=unames)
ratings = pd.read_table('./movielens/ratings.dat', sep='::', header=None, names=rnames)
movies = pd.read_table('./movielens/movies.dat', sep='::', header=None, names=mnames)

def three_merges(df1, df2, df3, key1, key2):
    merges = pd.merge(pd.merge(df1, df2, on=key1), df3, on=key2)
    return merges

def data_analysis(df):
    mean_ratings = df.pivot_table(values='rating', index='title', columns='gender', aggfunc='mean')
    ratings_by_title = df.groupby('title').size()
    active_titles = ratings_by_title.index[ratings_by_title >= 250]
    mean_ratings = mean_ratings.loc[active_titles]
    top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
    print('top10 movie ratings by female is {}'.format(top_female_ratings[:10]))
    mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
    sorted_by_diff = mean_ratings.sort_values(by='diff')
    print('top10 diff is {}'.format(sorted_by_diff[:10]))


if __name__ == "__main__":
    data = three_merges(users, ratings, movies, 'user_id', 'movie_id')
    data_analysis(data)
