import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Prepare the data for random walk
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Show random walk points
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    point_numbers = range(rw.num_points)
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    ax.plot(rw.x_values, rw.y_values, linewidth=0.5)

    # Highlighting the first and last random walk points
    ax.scatter(0, 0, c='green', edgecolor='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # Hide the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Do you wanna create another random walk? (Y/n): ")
    if keep_running == 'n':
        break
