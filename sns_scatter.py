# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:58:55 2020

@author: Muhammad Waqas
"""
import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset("titanic")
sns.scatterplot(df.survived,df.age,data=df,hue="who",style="who",size="who")
df.age.count()