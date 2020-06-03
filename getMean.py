import classifyTime as ct
import datetime

startOfCurrentDay = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)


currentTimePlus = startOfCurrentDay

# Get mean ot csv file at 00:00
ct.classifyTime(currentTimePlus, 'randomTimePrice.csv', 'analysis')

# Get mean every 30 minutes of that day
for i in range(47):
    currentTimePlus = currentTimePlus + datetime.timedelta(minutes=30)
    print(currentTimePlus)
    ct.classifyTime(currentTimePlus, 'randomTimePrice.csv', 'analysis')


