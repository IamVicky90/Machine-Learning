# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:07:51 2020

@author: Muhammad Waqas
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

plt.figure(figsize=(14,17))
plt.subplot(321)
np.random.seed(42)
s1_std_mar=np.random.randint(60,90,200)
s2_std_mar=np.random.randint(50,80,200)
# plt.figure(figsize=(16,9))
plt.style.use("ggplot")
plt.xlabel("Marks of students",)
plt.ylabel("Number of students")
plt.title("Histogram of student's marks for section A & B")
plt.hist([s1_std_mar,s2_std_mar],bins=[60,65,70,70,80,85,90],rwidth=0.8,label=["Section A Students Marks","Section B Students Marks"])
plt.legend()

plt.subplot(322)



# plt.figure(figsize=(15,10))
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

plt.subplot(323)


plt.style.available
# style.use("ggplot")
style.use('seaborn-deep')
x=np.array([1,2,3,4,5,6,7])
m_weather=np.array([25,35,45,43,27,35,20])
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid(color="r",linestyle=":")
plt.title("Multan & Lahore Weakly Weather Report")
plt.plot(x,m_weather,'go:',label="Multan Weather")
# plt.legend(loc="lower left")
l_weather=np.array([20,37,40,37,46,43,23])
plt.plot(x,l_weather,'ro:',label="Lahore Weather")
plt.legend(loc="lower center")



plt.subplot(324)


data=pd.read_csv("datasets_582631_1175383_UNCOVER_New_York_Times_covid-19-state-level-data.csv")
x=data["cases"]
y=data["deaths"]
plt.xlabel("No of cases")
plt.ylabel("No of deaths and number of fips")
plt.title("Coronavirus cases and deaths")
# plt.figure(figsize=(15,10))
plt.scatter(x,data["fips"],marker="*",label="No of Fips")
plt.scatter(x,y,label="Number of deaths")
plt.legend()



plt.subplot(325)


classes =np.array(["Python","R","Java","JavaScript","C#"])
students =np.array([70,54,34,50,56])

plt.pie(students,labels=classes,autopct='%.2f%%',explode=[0.3,0,0,0,0])
plt.legend(loc=3)

plt.subplot(326,polar=True,facecolor="k")




plt.savefig("savefig sub plot")
plt.show()
