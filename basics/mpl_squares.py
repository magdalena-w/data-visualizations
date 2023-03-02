import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8-poster')

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Define the chart title and axis labels
ax.set_title("Squares of numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares of values", fontsize=14)

# Defining the size of the labels
ax.tick_params(axis='both', labelsize=14)

plt.show()

print(plt.style.available)
