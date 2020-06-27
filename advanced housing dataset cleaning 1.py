# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 17:20:42 2020

@author: Muhammad Waqas
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("train.csv")
plt.figure(figsize=(25,25))
sns.heatmap(df.isnull())
null_var=df.isnull().sum()/df.shape[0]*100
df2_rm_null_col=df.drop(null_var[null_var]>17,axis=1)
