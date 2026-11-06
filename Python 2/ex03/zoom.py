import matplotlib.pyplot as plt
from load_image import ft_load


def zoom(image):
    """Return a 400x400 crop of the face with one channel."""
    # image[rows, columns, channels]: rows 100-499 (Y), columns 450-849 (X),
    # channel 0:1 keeps the 3rd axis -> (400, 400, 1).
    return image[100:500, 450:850, 0:1]


def main():
    """Load animal.jpeg, zoom on it and display the result."""
    try:
        image = ft_load("animal.jpeg")
        if image is None:
            return
        print(image)

        zoomed = zoom(image)
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)

        # imshow cannot draw a (400, 400, 1) array, it wants (400, 400)
        # for grayscale: squeeze() removes the dimension of size 1.
        # cmap="gray" tells matplotlib to draw values as shades of grey
        plt.imshow(zoomed.squeeze(), cmap="gray")
        plt.show()
    except Exception as error:
        # Catch-all so the program never stops abruptly
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
