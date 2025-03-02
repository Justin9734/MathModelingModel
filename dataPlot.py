import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')

fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')
ax.set_title('3D Parametric Plot')


ax.set_xlabel('Temp (f)', labelpad=20)
ax.set_ylabel('Power Consumption', labelpad=20)
ax.set_zlabel('Year', labelpad=20)

im_lazy_year = [2023, 2022, 2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000]
im_lazy_power_con = []
im_lazy_temp = [102,102,96,97,100,97,99,100,99,100,98,103,106,104,100,101,106,102,100,97,98,98,96,107]
for x in range(0, 24):
    ax.plot3D(im_lazy_temp[x], 0, im_lazy_year[x], ".")
plt.show()

#print(len(im_lazy_year))
#print(len(im_lazy_temp))
print("Done!")