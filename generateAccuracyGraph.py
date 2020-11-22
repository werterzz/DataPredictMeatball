import random
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as md
import matplotlib.ticker as ticker
import matplotlib.dates as mdates

timeShedule = []
frontTime = "00"
backTime = "00"
backTimeFlag = 0
frontTimecount = 0

for i in range(48):
    
    if i % 2 == 0:
        if frontTimecount < 10:
            frontTime = "0" + str(frontTimecount)
        else:
            frontTime = str(frontTimecount)
        frontTimecount += 1
    if backTimeFlag == 0:
        backTimeFlag = 1
        backTime = "00"
    else:
        backTimeFlag = 0
        backTime = "30"
    timeShedule.append(frontTime + ":" + backTime)


print(timeShedule)

df = pd.read_csv (r'testAccuracy.csv')

guess = df['guess'].values
actual = df['actual'].values

ax = plt.gca()
ax.axes.xaxis.set_ticks([0, 6, 12, 18, 24, 30, 36, 42, 48])

plt.plot(timeShedule, guess, label = "guess")
plt.plot(timeShedule, actual, label = "actual")
plt.text(20, 155, "Absolute Mean Error: 36.04")
plt.text(20, 135, "7 Day Previous Mean: 0.5023")
plt.text(20, 115, "Day Of Week Mean: 0.1283")

plt.xlabel('time')
# Set the y axis label of the current axis.
plt.ylabel('total price')
# Set a title of the current axes.
plt.title('guess & actual comparing graph')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()