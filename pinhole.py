import matplotlib.pyplot as plt


def generate_holes_file():
    # Define parameters
    larger_square_size = 43.5
    hole_size = 1.2
    skip_size = 0.3

    # Calculate the number of holes needed in each row and column
    rows = int(larger_square_size / (hole_size + skip_size))
    cols = int(larger_square_size / (hole_size + skip_size))

    # Calculate the starting point for the holes to center them
    start_x = (larger_square_size - cols * (hole_size + skip_size) + skip_size) / 2
    start_y = (larger_square_size - rows * (hole_size + skip_size) + skip_size) / 2

    # Open a file for writing
    with open("holes_coordinates.txt", "w") as file:
        # Loop through each row and column to generate coordinates
        for row in range(rows):
            for col in range(cols):
                # Calculate the coordinates for each hole center
                x = start_x + col * (hole_size + skip_size)
                y = start_y + row * (hole_size + skip_size)

                # Write the coordinates to the file
                file.write(f"{x:.2f}, {y:.2f}\n")


def plot_holes():
    # Read coordinates from the file
    with open("holes_coordinates.txt", "r") as file:
        lines = file.readlines()
        hole_coordinates = [
            tuple(map(float, line.strip().split(","))) for line in lines
        ]

    # Visualize the holes
    for coordinate in hole_coordinates:
        plt.scatter(coordinate[0], coordinate[1], color="red", s=5)

    plt.gca().set_aspect("equal", adjustable="box")
    plt.savefig("pinhole.png")


if __name__ == "__main__":
    generate_holes_file()
    plot_holes()
