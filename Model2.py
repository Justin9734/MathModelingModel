import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import csv
from sklearn.linear_model import LinearRegression
import pandas as pd
with open('ElecSales.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    
# Data formatting
data_array = np.array(data, dtype="object")
data_array = np.delete(data_array, [0, 1, 2, 3,4])
data_array=np.vstack(data_array)

allowed_months = {"Jun", "Jul", "Aug"}
mask = np.any([np.char.find(data_array[:, 0], keyword) >= 0 for keyword in allowed_months], axis=0)
filtered_arr = data_array[mask]
group_size = 3
new_length = len(filtered_arr) // group_size
combined_values = np.add.reduceat(filtered_arr[:, 1].astype(float), np.arange(0, len(filtered_arr), group_size))
new_first_column = np.array(["".join(str(filtered_arr[i:i+group_size, 0])[6:10]) for i in range(0, len(filtered_arr), group_size)])
averageResidentialUsageDuringSummerMonths = np.column_stack((new_first_column, combined_values))

memphisUsageRatio = 15172 / 10791
#print (memphisUsageRatio) # the average mephisian uses about 1.4 times more power than the average american
NUMPERHOUSE = 2.42
# https://www.macrotrends.net/global-metrics/cities/23063/memphis/population
MemphisPopNumber = {2025:1188000, 2024:1179000, 2023:1170000, 2022:1163000, 2021:1156000, 2020:1150000, 2019:1144000, 2018:1139000, 2017:1129000, 2016:1119000, 2015:1109000, 2014:1100000, 2013:1090000, 2012:1081000, 2011:1072000, 2010:1062000, 2009:1053000, 2008:1044000, 2007:1035000, 2006:1026000, 2005:1017000, 2004:1009000, 2003:1000000, 2002:991000, 2001:983000, 2000:974000, 1999:960000, 1998:945000, 1997:929000}
MemphisResCount = {} # the approximate residential count in Memphis (prob like p = 10 or som idk i forgor p values)
MemphisSummerUsage = {}
x = 0 # i would NEVER EVER make a stupid workaround
for i in MemphisPopNumber:
    MemphisResCount[i] = MemphisPopNumber[i]/NUMPERHOUSE
    MemphisSummerUsage[i] = MemphisResCount[i] * float(averageResidentialUsageDuringSummerMonths[x][1]) * memphisUsageRatio
    x+=1
#Source: THE DOC
MemphisHighTemps = {2023:102, 2022:102, 2021:96, 2020:97, 2019:100, 2018:97, 2017:99, 2016:100, 2015:99, 2014:100, 2013:98, 2012:103, 2011:106, 2010:104, 2009:100, 2008:101, 2007: 106, 2006:102, 2005:100, 2004:97, 2003:98, 2002:98, 2001:96, 2000:107}

X = []
Y = []
for i in MemphisHighTemps: # the model is predicting the summer usage based off the year and high temp
    
    X.append([])
    X[-1].append(MemphisHighTemps[i]) 
    X[-1].append(i)
    Y.append(MemphisSummerUsage[i])
X = np.array(X)
Y = np.array(Y)
model = LinearRegression()
model.fit(X, Y)
print(model.coef_)


