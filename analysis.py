import getMean

def analysis():
    a, b, bias = getMean.getMean()
    print(f"PreviousMeanWeight: {a}, WeekDayMean: {b}, bias: {bias}")
    return a, b, bias
