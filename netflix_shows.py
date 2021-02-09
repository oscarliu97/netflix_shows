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
import plotly.graph_objects as go
from collections import Counter

netflix_shows = pd.read_csv("netflix_titles.csv")

netflix_shows['genre'] = netflix_shows['listed_in'].apply(lambda x :  x.replace(' ,',',').replace(', ',',').split(',')) 
# country_df = country_df[country_df['principal_country'] /  country_df['principal_country'].sum() > 0.01]
d2 = netflix_shows[netflix_shows['type'] == 'Movie']
col = "listed_in"
categories = ", ".join(d2['listed_in']).split(", ")
counter_list = Counter(categories).most_common(50)
labels = [_[0] for _ in counter_list][::-1]
values = [_[1] for _ in counter_list][::-1]
trace1 = go.Bar(y=labels, x=values, orientation="h", name="TV Shows", marker=dict(color="#a678de"))

data = [trace1]
layout = go.Layout(title="Content added over the years", legend=dict(x=0.1, y=1.1, orientation="h"))
fig = go.Figure(data, layout=layout)
fig.show()

text = str(list(d2['genre'])).replace(',', '').replace('[', '').replace("'", '').replace(']', '')