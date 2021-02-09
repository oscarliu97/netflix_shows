#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 10:31:16 2021

@author: oscarliu
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

netflix_shows = pd.read_csv("netflix_titles.csv")

netflix_date = netflix_shows[['date_added']].dropna()
netflix_date['year'] = netflix_date['date_added'].apply(lambda x : x.split(', ')[-1])
netflix_date['month'] = netflix_date['date_added'].apply(lambda x : x.lstrip().split(' ')[0])
netflix_shows['principal_country'] = netflix_shows['country'].apply(lambda x: x.split(",")[0])
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'][::-1]
df = netflix_date.groupby('year')['month'].value_counts().unstack().fillna(0)[month_order].T
plt.figure(figsize=(10, 7), dpi=200)
plt.pcolor(df, cmap='afmhot_r', edgecolors='white', linewidths=2) # heatmap
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns, fontsize=7, fontfamily='serif')
plt.yticks(np.arange(0.5, len(df.index), 1), df.index, fontsize=7, fontfamily='serif')

plt.title('Netflix Contents Update', fontsize=12, fontfamily='calibri', fontweight='bold', position=(0.20, 1.0+0.02))
cbar = plt.colorbar()

cbar.ax.tick_params(labelsize=8) 
cbar.ax.minorticks_on()
plt.show()
a = np.arange(0.5, len(df.columns), 1)
ratings_ages = {
    'TV-PG': 'Older Kids',
    'TV-MA': 'Adults',
    'TV-Y7-FV': 'Older Kids',
    'TV-Y7': 'Older Kids',
    'TV-14': 'Teens',
    'R': 'Adults',
    'TV-Y': 'Kids',
    'NR': 'Adults',
    'PG-13': 'Teens',
    'TV-G': 'Kids',
    'PG': 'Older Kids',
    'G': 'Kids',
    'UR': 'Adults',
    'NC-17': 'Adults'
}
netflix_shows['target_ages'] = netflix_shows['rating'].replace(ratings_ages)
rating_df = netflix_shows.groupby(['rating', 'target_ages']).agg({'show_id': 'count'}).reset_index()
rating_df.columns = ['rating','target_ages','count']
rating_df = rating_df.sort_values('target_ages')

country_df = df['principal_country'].value_counts().reset_index()
# country_df = country_df[country_df['principal_country'] /  country_df['principal_country'].sum() > 0.01]

netflix_shows
