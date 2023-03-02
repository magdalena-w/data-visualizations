import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Define the chart title and axis labels
ax.set_title("Squares of numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Squares of values", fontsize=14)

# Define a range for each axis
ax.axis = ([0, 1100, 0, 1100000])

# If you want to disable both the offset and scientific notation, you'd use
ax.ticklabel_format(useOffset=False, style='plain')

plt.show()
