import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('data.csv')


data['datetime'] = pd.to_datetime(data['datetime'])


date = data['datetime'].dt.date.astype('category').cat.codes  
time = data['datetime'].dt.hour  
tempmin = data['tempmin']


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.scatter(date, time, tempmin, c=tempmin, cmap='coolwarm')


ax.set_xlabel('Date')
ax.set_ylabel('Hour of Day')
ax.set_zlabel('Minimum Temperature')
ax.set_title("3D Weather Report")

plt.show()
