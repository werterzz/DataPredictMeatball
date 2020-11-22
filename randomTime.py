import random
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as md
import matplotlib.ticker as ticker
import matplotlib.dates as mdates

def random_date(start, l):
   current = start
   while l > 0:

    randMin = [10, 30, 60, 120, 240]
    randMin = random.choices(randMin, weights=[0.5, 1, 2, 4, 16])
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
    # print(randMin)
    current = current + \
        datetime.timedelta(minutes=random.randrange(initMin, randMin[0]))
    yield current
    l -= 1


def generateGraphWeekday(randomTime, order):
    for i in range(len(randomTime)):
        randomTime[i] = datetime.datetime.strptime(randomTime[i], "%y/%m/%d %H:%M")
        # currentTime = datetime.datetime.now()
        # randomTime[i] = randomTime[i].replace(year=currentTime.year, month=currentTime.month, day=currentTime.day)
    
    timeShedule = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT','SUN']

    orderCountBinning = []
    for i in range(7):
        orderCountBinning.append(0)
    for x in randomTime:
        for i in range(7):
            if x.weekday() == i:
                orderCountBinning[i] += 1 
    # ax = plt.gca()
    # ax.axes.xaxis.set_ticks([0, 6, 12, 18, 24, 30, 36, 42, 48])
    # randomTime = matplotlib.dates.date2num(randomTime)
    # plt.scatter(randomTime, order, label="stars", color="green", marker="1", s=3)
    plt.bar(timeShedule, orderCountBinning, color='green')
    # plt.plot(randomTime, order)
    plt.xlabel('Day Of Week')
    plt.ylabel('Total Price')

    plt.title('Numbers of order in specific day')

    plt.show()

    

def generateGraph(randomTime, order):
    for i in range(len(randomTime)):
        randomTime[i] = datetime.datetime.strptime(randomTime[i], "%y/%m/%d %H:%M")
        currentTime = datetime.datetime.now()
        randomTime[i] = randomTime[i].replace(year=currentTime.year, month=currentTime.month, day=currentTime.day)

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




    # Count order every 30 mins for binning to the graph
    orderCountBinning = []
    for i in range(48):
        orderCountBinning.append(0)

    for x in randomTime:
        for i in range(48):
            startCheckTime = currentTime.replace(hour=0, minute=0) + datetime.timedelta(minutes=30*i)
            endCheckTime = currentTime.replace(hour=0, minute=30) + datetime.timedelta(minutes=30*i)
            if x >= startCheckTime and x <= endCheckTime:
                orderCountBinning[i] += 1 

    print(orderCountBinning)

 

    # randomTime = randomTime[800:900]
    # order = order[800:900]

    # print(randomTime)

    # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax = plt.gca()
    ax.axes.xaxis.set_ticks([0, 6, 12, 18, 24, 30, 36, 42, 48])
    # randomTime = matplotlib.dates.date2num(randomTime)
    # plt.scatter(randomTime, order, label="stars", color="green", marker="1", s=3)
    plt.bar(timeShedule, orderCountBinning, color='green')
    # plt.plot(randomTime, order)
    plt.xlabel('Time')
    plt.ylabel('Total Price')

    plt.title('Numbers of order in specific time')

    plt.show()

def randomWeekdayDataSet(start, l):
    current = start
    ruleDate = start.weekday()
    while l > 0:
        checkInRange = True
        if current.weekday() == ruleDate:
            checkInRange = True
        else:
            checkInRange = False
    
        if checkInRange == True:
            randMin =  random.randint(0, 11)
            current = current + datetime.timedelta(minutes=randMin)             

        else:    
            randMin =  random.randint(30, 120)
            current = current + datetime.timedelta(minutes=randMin)
        yield current
        l -= 1


# Random order to most of order can be in range base on ruleDate (ruleDate are same on everyday)
def randomRealDataSet(start, l):
    current = start
    # Set rule to random minute out of range rule date
    

    while l > 0:
        ruleDate = [[current.replace(hour=8, minute=0), current.replace(hour=9, minute=0)], [current.replace(hour=12, minute=0), current.replace(hour=13, minute=0)] , [current.replace(hour=16, minute=0), current.replace(hour=17, minute=0)]  ]
        checkInRange = True
        for i in range(len(ruleDate)):
            if current >= ruleDate[i][0] and current <= ruleDate[i][1]:
                checkInRange = True
                break
            else:
                checkInRange = False
    
        if checkInRange == True:
            randMin =  random.randint(0, 6)
            current = current + datetime.timedelta(minutes=randMin)             

        else:    
            while 1:
                randMin =  random.randint(0, 60)
                temp = current
                current = current + datetime.timedelta(minutes=randMin) 
                if current <= ruleDate[0][0]:
                    break
                elif current >= ruleDate[0][1] and current <= ruleDate[1][0]:
                    break
                elif current >= ruleDate[1][1] and current <= ruleDate[2][0]:
                    break
                elif current >= ruleDate[2][1]:
                    break
                else:
                    current = temp
        yield current
        l -= 1
# Generate random data to csv file

startDate = datetime.datetime(2020, 10, 1, 6, 00)

randomTime = []


for x in (list(randomRealDataSet(startDate,4000))):

    randomTime.append(x.strftime("%y/%m/%d %H:%M"))

order = []
for x in range(4000):
    order.append(int(random.choices([20, 30], [2, 1])[0]))


data = list(zip(randomTime, order))

generateGraph(randomTime, order)

df = pd.DataFrame(data = data, columns=['Time', 'orderPrice'])
df.to_csv('./randomTimePrice.csv', index=False, header=True)