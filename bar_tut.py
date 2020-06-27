# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 00:38:40 2020

@author: Muhammad Waqas
"""
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(15,10))
c_sub=np.array(["Python","Java","JavaScript","C#","C++"])
c1_std=np.array([80,30,75,80,74])
c2_std=np.array([90,25,70,85,34])
c3_std=np.array([88,34,79,83,37])
len_c_sub=np.arange(len(c_sub))

width=0.2
plt.bar(len_c_sub,c1_std,width=width,label="Class 1 Students",edgecolor="r")
plt.bar(len_c_sub+width,c2_std,width=width,label="Class 2 Students")
plt.bar(len_c_sub+width+width,c3_std,width=width,label="Class 3 Students")
plt.legend()
plt.xticks(len_c_sub,c_sub,rotation=14)


