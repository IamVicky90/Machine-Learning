# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:14:14 2020

@author: Muhammad Waqas
"""
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
s1_std_mar=np.random.randint(60,90,200)
s2_std_mar=np.random.randint(50,80,200)
plt.figure(figsize=(16,9))
plt.style.use("ggplot")
plt.xlabel("Marks of students",size=30)
plt.ylabel("Number of students",size=(30))
plt.title("Histogram of student's marks for section A & B", size=35)
plt.hist([s1_std_mar,s2_std_mar],bins=[60,65,70,70,80,85,90],rwidth=0.8,label=["Section A Students Marks","Section B Students Marks"])
plt.legend()
