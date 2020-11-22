import matplotlib.pyplot as plt

# Create a Simple Bar Plot of Three People's Ages

# Create a List of Labels for x-axis
names = ["Brad", "Bill", "Bob"]

# Create a List of Values (Same Length as Names List)
ages = [9, 5, 10]

# Make the Chart
plt.bar(names, ages)

# Show the Chart
plt.show()