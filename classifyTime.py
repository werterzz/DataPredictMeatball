import pandas as pd # Used for manipulate with csv file
import datetime # Used for time control
import matplotlib.pyplot as plt
import matplotlib

'''
This function is used for two purpose
one is used for getting previous 7 day mean and weekday mean (eg. every monday mean) in specific 30 minutes at that time
for compute mean to prepare food in specific time
two is used for getting previous mean, weekday mean and actual result to csv file for analysis weighted of two mean
parameter Time is datetime type to compute specific time, file(string) is name of input data csv file, mode(string) is 
options to use this function have two options: "compute", "analysis"
'''
def classifyTime(Time, file, mode):
    # Read data from file
    df = pd.read_csv(file)
    
    # Get current date and set to file format
    currentDate = Time
    currentDateStr = currentDate.strftime("%y/%m/%d %H:%M")
    print(currentDate)

    # Used for check minute in checkMin()
    minuteFocus = currentDate.minute

    # Check the time is over 30 minutes or not
    def checkMin(minute):
        if minuteFocus >= 0 and minuteFocus < 30:
            if minute < 30: return 1
            else: return 0
        elif minuteFocus >= 30 and minuteFocus <= 59:
            if minute >= 30: return 1
            else: return 0
        
    filterDf = {
        'Time': [],
        'orderPrice' : []
    }

    # Filter time specific hour and minute in everyday
    for index, row in df.iterrows():
        time = datetime.datetime.strptime(row['Time'], "%y/%m/%d %H:%M")
        if time.hour == currentDate.hour:
            if(checkMin(time.minute)): 
                filterDf['Time'].append(row['Time'])
                filterDf['orderPrice'].append(row['orderPrice'])

    df = pd.DataFrame(filterDf, columns = ['Time', 'orderPrice'])
    # print(df)

    # Get previous date 2 day and set to file format
    previous8Days = datetime.datetime.now() - datetime.timedelta(days=8)
    previous8Days = previous8Days.strftime("%y/%m/%d %H:%M")
    

    def generateGraph(randomTime, order):
        for i in range(len(randomTime)):
            randomTime[i] = datetime.datetime.strptime(randomTime[i], "%y/%m/%d %H:%M")
        randomTime = randomTime[:100]
        order = order[:100]
        print(order)
        randomTime = matplotlib.dates.date2num(randomTime)
        plt.scatter(randomTime, order, label="stars", color="green", marker="1", s=3)
        # plt.plot(randomTime, order)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')

        plt.title('Line graph!')

        plt.show()
    
    
    # Result is current date - num of days
    def convertToPreviousDayStr(num):
        previous = datetime.datetime.now() - datetime.timedelta(days=num)
        previous = previous.strftime("%y/%m/%d")
        return previous

    
    actual = 0 # Value actual sum of purchase in 30 minutes
    currentDay = currentDate.strftime("%y/%m/%d")

    # Sum orderPrice in 30 minutes current date
    for index, row in df.iterrows():
        temp = datetime.datetime.strptime(row['Time'], "%y/%m/%d %H:%M")
        tempDay = temp.strftime('%y/%m/%d')
        if tempDay == currentDay: actual = actual + row['orderPrice']

    print("Actual: {}".format(actual))
    # print(df["Time"][0])
    # Filter currect date to previous 7 date from file
    selected = df[(df['Time'] < currentDateStr) & (df['Time'] >= previous8Days)]
    

    # Add orderPrice to array if time is equal to previous day
    def checkCountOrderInTime(num, prevDay, rowTime):
        
        if rowTime == convertToPreviousDayStr(num): 
            prevDay[num-1] = prevDay[num-1] + row['orderPrice']
        return prevDay

    sum=0 # Used for previous mean
    prevDay = [0, 0, 0, 0, 0, 0, 0]

    # Check previous 7 day in specific 30 minute time if have order: add orderPrice to array
    for index, row in selected.iterrows():
        for i in range(1, 8):
            time = datetime.datetime.strptime(row['Time'], "%y/%m/%d %H:%M")
            time = time.strftime("%y/%m/%d")
            prevDay = checkCountOrderInTime(i, prevDay, time)
    
    # Sum orderPrice of previous mean and calculate
    for i in prevDay:
        sum = sum + i
    previousMean = sum/7
    print("Previous Mean: {}".format(previousMean))



    weekdayDate = {
        'Time': [],
        'orderPrice' : []
    }

    # Append Time and orderPrice to weekdayDate array
    def appendDay(time, orderPrice, weekday):
        weekday['Time'].append(time)
        weekday['orderPrice'].append(orderPrice)
        return weekday

    # Classify weekday to array
    for index, row in df.iterrows():
        temp = datetime.datetime.strptime(row['Time'], "%y/%m/%d %H:%M")
        tempDate = temp.strftime("%y/%m/%d")
        currentDateSpec = currentDate.strftime("%y/%m/%d")
        previous4Week = currentDate - datetime.timedelta(days=29)
        weekdayTemp = temp.weekday()

        # Used 4 week previous of that day (eg. 4 previous monday not include current monday)    
        if temp >= previous4Week and tempDate < currentDateSpec and weekdayTemp == currentDate.weekday(): weekdayDate = appendDay(row['Time'], row['orderPrice'], weekdayDate)
        

    weekdayDate = pd.DataFrame(weekdayDate, columns = ['Time', 'orderPrice'])
    
    checkDate = [] # keep date appear in 4 week equal to current weekday
    check = -1 # used for checking index date in array

    # Classify time in weekday
    for index, row in weekdayDate.iterrows():
        temp = datetime.datetime.strptime(row['Time'], "%y/%m/%d %H:%M")
        tempDay = temp.strftime("%y/%m/%d")
        check = -1
    
        for i in range(len(checkDate)):
            if checkDate[i]['Time'] == tempDay:
                check = i
        if check == -1:
            checkDate.append({'Time': tempDay, 'orderPrice': row['orderPrice']})
        else:
            checkDate[check]['orderPrice'] = checkDate[check]['orderPrice'] + row['orderPrice']
    

    weekdayDate = pd.DataFrame(checkDate, columns = ['Time', 'orderPrice'])

    sum = 0 # sum of weekday mean

    # Sum orderPrice in weekday can calculate weekday mean
    for index, row in weekdayDate.iterrows():
        sum = sum + row['orderPrice']
    weekDayMean = sum/4
    print("Weekday Mean: {}".format(weekDayMean))

    data = {'PreviousMean': [previousMean], 'WeekDayMean': [weekDayMean], 'Actual': [actual]}

    df = pd.DataFrame(data, columns= ['PreviousMean', 'WeekDayMean', 'Actual'])



    if mode == 'compute':
        return df
    elif mode == 'analysis':
        df.to_csv('mean.csv', mode='a', header=False, index=False) 
        