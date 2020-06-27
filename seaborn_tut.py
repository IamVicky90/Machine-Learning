# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:00:25 2020

@author: Muhammad Waqas
"""
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("DataSet.csv")
df=df.fillna(df.mean())
sns.lineplot(x="Age",y="Salary",data=df,hue="Married",markers=["o","<"],style="Married",legend="full ")
plt.show()
