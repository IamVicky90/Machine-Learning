# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:34:32 2020

@author: Muhammad Waqas
"""
import matplotlib.pyplot as plt
# import numpy as np
import pandas as pd
data=pd.read_csv("datasets_582631_1175383_UNCOVER_New_York_Times_covid-19-state-level-data.csv")
x=data["cases"]
y=data["deaths"]
plt.xlabel("No of cases")
plt.ylabel("No of deaths and number of fips")
plt.title("Coronavirus cases and deaths")
plt.figure(figsize=(15,10))
plt.scatter(x,data["fips"],marker="*",label="No of Fips")
plt.scatter(x,y,label="Number of deaths")
plt.legend()