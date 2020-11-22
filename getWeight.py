import pandas as pd


def getWeight():

    df = pd.read_csv("mean.csv")

    '''

    for more information of gradient descent https://www.youtube.com/watch?v=jc2IthslyzM
    '''

    a = 0.5 # Weight of PreviousMean
    b = 0.5 # Weight of WeekDayMean
    bias = -1.2 # Change value for directly minimize error
    learningRate = 0.00000001 # Decrease learningRate when error not decrease, execution time inverse to learningRate
    error = 0
    epoch = 1000 # number of iterration to compute all data

    for order in range(epoch): # Loop to compute all data
        for index, row in df.iterrows(): # Compute each row
            guess = a*row["PreviousMean"] + b*row["WeekDayMean"] + bias # ax1 + bx2 + bias
            error = row["Actual"] - guess

            # Compute weight with gradient descent
            a = a + error*row["PreviousMean"]*learningRate
            b = b + error*row["WeekDayMean"]*learningRate
            bias = bias + error*learningRate

        # Print error every 1000 epoch        
        if order % 1000 == 0:
            print(error)

    print(f"PreviousMeanWeight: {a}, WeekDayMean: {b}, bias: {bias}")

    count = 0 # Count for correct prediction

    guessArray = []
    actualArray = []
    error = 0

    # Loop all data to get prediction
    for index, row in df.iterrows():
        guess = a*row["PreviousMean"] + b*row["WeekDayMean"] + bias
        # loop for normalize guess value
        # for i in range(10):
        #     if guess >= 10+(i*10):
        #         if guess < 20: guess = 20
        #         elif guess < 10 + ((i-1)*10) + 5: guess = i*10 
        #         else : guess = 10 + (i*10)
        #     elif guess < 10: guess = 0
        guess = guess//10 * 10
        if guess < 0: guess = 0

        # print(guess, row["Actual"])
        guessArray.append(guess)
        actualArray.append(row["Actual"])

        testAccuracy = {'guess': guessArray, 'actual': actualArray}
        testAccuracyDF = pd.DataFrame(testAccuracy, columns=['guess', 'actual'])
        testAccuracyDF.to_csv(r'testAccuracy.csv', index = False, header=True)

        error = error + abs(guess - row["Actual"])
    error = error/len(df) 
    print(f"Error: {error} ")
    return a, b, bias