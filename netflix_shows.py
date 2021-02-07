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

df = pd.read_csv("netflix_titles.csv")

order=df['rating'].value_counts().index[0:14]

