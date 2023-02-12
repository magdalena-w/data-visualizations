import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Prepare the data for random walk
    rw = RandomWalk(100_000)
    rw.fill_walk()

    # Show random walk points  seaborn-v0_8
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Highlighting the first and last random walk points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Hide the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Do you wanna create another random walk? (Y/n): ")
    if keep_running == 'n':
        break
