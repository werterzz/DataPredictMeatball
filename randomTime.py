import random
import datetime 
import pandas as pd

def random_date(start,l):
   current = start
   while l > 0:

    randMin = [10, 30, 60, 120, 240]
    randMin =  random.choices(randMin, weights=[0.5, 1, 2, 4, 16])
    initMin = 0
    if randMin == 10:
        initMin = 0
    elif randMin == 30:
        initMin = 10
    elif randMin == 60:
        initMin = 30
    elif randMin == 120:
        initMin = 60
    elif randMin == 240:
        initMin = 120
    current = current + datetime.timedelta(minutes=random.randrange(initMin, randMin[0]))
    yield current
    l-=1


# Generate random data to csv file

startDate = datetime.datetime(2020, 4, 20, 6, 00)

randomTime = []

for x in (list(random_date(startDate,1000))):

    randomTime.append(x.strftime("%y/%m/%d %H:%M"))

order = []
for x in range(1000):
    order.append(int(random.choices([20, 30], [2, 1])[0]))


data = list(zip(randomTime, order))
print(data)

df = pd.DataFrame(data = data, columns=['Time', 'orderPrice'])
df.to_csv('./randomTimePrice.csv', index=False, header=True)
