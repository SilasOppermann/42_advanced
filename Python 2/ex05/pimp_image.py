import numpy as np
import matplotlib.pyplot as plt


def _show(array: np.ndarray, title: str) -> None:
    """Display an image in a matplotlib window with a title."""
    plt.imshow(array)
    plt.title(title)
    plt.show()


# Reminder: an RGB image is an array of shape (height, width, 3).
#   array[:, :, 0] -> all the Red values
#   array[:, :, 1] -> all the Green values
#   array[:, :, 2] -> all the Blue values
# ":" means "every index along that axis".
# Every function works on a COPY so the original image is never changed
# (the tester reuses the same array for all 5 filters).


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received.

    Allowed operators: =, +, -, *
    Each value v (0-255) becomes 255 - v: black <-> white, etc.
    """
    result = 255 - array        # numpy applies it to every value at once
    _show(result, "Invert")
    return result


def ft_red(array) -> np.ndarray:
    """Keep only the red channel of the image (green and blue = 0).

    Allowed operators: =, *
    Multiplying by [1, 0, 0] keeps R and zeroes G and B for every pixel
    ("broadcasting": numpy repeats [1, 0, 0] for each pixel).
    """
    result = (array * [1, 0, 0]).astype(np.uint8)
    _show(result, "Red")
    return result


def ft_green(array) -> np.ndarray:
    """Keep only the green channel of the image (red and blue = 0).

    Allowed operators: =, -
    A channel minus itself is 0, which removes it.
    """
    result = array.copy()
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
    _show(result, "Green")
    return result


def ft_blue(array) -> np.ndarray:
    """Keep only the blue channel of the image (red and green = 0).

    Allowed operators: =
    We simply assign 0 to the red and green channels.
    """
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    _show(result, "Blue")
    return result


def ft_grey(array) -> np.ndarray:
    """Convert the image to grey, keeping the (height, width, 3) shape.

    Allowed operators: =, /
    Grey = average of R, G and B. We cannot write (R + G + B) / 3
    because "+" is not allowed, but np.sum is a function, not an
    operator. The same grey value is then put in all 3 channels
    (when R == G == B the color is a shade of grey).
    """
    grey = (np.sum(array, axis=2) / 3).astype(np.uint8)   # (h, w)
    result = array.copy()
    result[:, :, 0] = grey
    result[:, :, 1] = grey
    result[:, :, 2] = grey
    _show(result, "Grey")
    return result


def main():
    """Nothing to run: this file is a module meant to be imported."""
    pass


if __name__ == "__main__":
    main()
