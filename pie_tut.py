# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:37:41 2020

@author: Muhammad Waqas
"""
import matplotlib.pyplot as plt
import numpy as np
classes =np.array(["Python","R","Java","JavaScript","C#"])
students =np.array([70,54,34,50,56])

plt.pie(students,labels=classes,autopct='%.2f%%',explode=[0.3,0,0,0,0])
plt.legend(loc=3)

