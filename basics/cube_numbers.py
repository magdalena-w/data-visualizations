import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.PuBu, s=10)

# Define the chart title and axis labels
ax.set_title("Cube numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cube numbers", fontsize=14)

# Define a range for each axis
ax.axis = ([0, 5000, 0, 125000000000])

# If you want to disable both the offset and scientific notation, you'd use
ax.ticklabel_format(useOffset=False, style='plain')

# Defining the size of the labels
ax.tick_params(axis='both', labelsize=7)

plt.show()
