import matplotlib.pyplot as plt
from load_image import ft_load


def zoom(image):
    """Cut a 400x400 square around the animal's face, keep one channel.

    Slicing a 3D array works axis by axis:  image[rows, columns, channels]
      - rows 100 to 499    (Y axis, top -> bottom)
      - columns 450 to 849 (X axis, left -> right)
      - channel 0:1        (only the red channel, but "0:1" instead of
                            "0" keeps the 3rd dimension -> (400, 400, 1))
    One channel = one value per pixel = a grayscale image.
    """
    return image[100:500, 450:850, 0:1]


def main():
    """Load animal.jpeg, print info, zoom on it and display the result."""
    try:
        image = ft_load("animal.jpeg")
        if image is None:       # ft_load already printed the error
            return
        print(image)

        zoomed = zoom(image)
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)

        # imshow cannot draw a (400, 400, 1) array, it wants (400, 400)
        # for grayscale: squeeze() removes the dimension of size 1.
        # cmap="gray" tells matplotlib to draw values as shades of grey
        # (by default it would use a green/purple color map).
        # The axes (scale on X and Y) are shown by default.
        plt.imshow(zoomed.squeeze(), cmap="gray")
        plt.show()
    except Exception as error:
        # Catch-all so the program never stops abruptly (subject rule).
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
