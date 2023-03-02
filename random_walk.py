from random import choice


class RandomWalk():
    """Class designed to generate a random walk."""

    def __init__(self, num_points=5000):
        """Initialization of attributes"""
        self.num_points = num_points

        # The starting point has coordinates (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Determine direction and the distance of the step and then create step"""
        # Determining the direction and the distance to be covered in that direction
        direction = choice([1, -1])  # Right or left
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance  # Length of the step, positive number - right, negative - left

        return step

    def fill_walk(self):
        """Generate all points for random walk"""
        # Performing steps until the expected number of points is reached
        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            # Rejection of moves that lead nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Determine next values of X and Y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


