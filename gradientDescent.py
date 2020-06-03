x = [[10, 10, 10, 10, 5], [10, 5, 10, 5, 5]]
y = [10, 7, 10, 7, 5]
a = 0.5
b = 0.5
bias = 1
learningRate = 0.005
error = 0

for order in range(5000):
    for i in range(len(x[0])):
        guess = a*x[0][i] + b*x[1][i] + bias
        error = y[i] - guess
        a = a + error*x[0][i]*learningRate
        b = b + error*x[1][i]*learningRate
        bias = bias + error*learningRate
    if order % 1000 == 0:
        print(error)
print(a, b)

for i in range(len(x[0])):
    guess = a*x[0][i] + b*x[1][i] + bias
    print(guess)