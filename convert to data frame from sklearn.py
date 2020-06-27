# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 19:43:56 2020

@author: Muhammad Waqas
"""
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
data=load_breast_cancer()
df = pd.DataFrame(data= np.c_[data['data'], data['target']],
                     columns= np.append(data['feature_names'] , ['target']))
plt.figure(figsize=(25,25))

sns.heatmap(df.corr(),annot=True,linewidth=3)