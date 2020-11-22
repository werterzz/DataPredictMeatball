import classifyTime as ct
import datetime
import analysis

def computeNow():
    # startOfCurrentDay = datetime.datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)


    # currentTimePlus = startOfCurrentDay
    currentTimePlus = datetime.datetime.now()

    data = ct.classifyTime(currentTimePlus, 'randomTimePrice.csv', 'compute')
    a, b, bias = analysis.analysis()
    predict = data["PreviousMean"].values[0]*a + data["WeekDayMean"].values[0]*b + bias
    print("PreviousMean value: {}".format(data["PreviousMean"].values[0]))
    print("WeekDayMean value: {}".format(data["WeekDayMean"].values[0]))
    print("predict value: {}".format(predict))
    print("Actual value: {}".format(data["Actual"].values[0]))
    return predict

computeNow()