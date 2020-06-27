import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
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
plt.show()