import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def _show(array: np.ndarray, title: str) -> None:
    """Display an image in a window with a title."""
    plt.imshow(array)
    plt.title(title)
    plt.show()


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    result = 255 - array
    _show(result, "Invert")
    return result


def ft_red(array) -> np.ndarray:
    """Keep only the red channel of the image."""
    #  .astype(np.uint8) is neccesary to not Upcast to int64
    result = (array * [1, 0, 0]).astype(np.uint8)
    _show(result, "Red")
    return result


def ft_green(array) -> np.ndarray:
    """Keep only the green channel of the image."""
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
    _show(result, "Green")
    return result


def ft_blue(array) -> np.ndarray:
    """Keep only the blue channel of the image."""
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    _show(result, "Blue")
    return result


def ft_grey(array) -> np.ndarray:
    """Convert the image to grey, keeping its shape."""
    grey = (np.sum(array, axis=2) / 3).astype(np.uint8)   # (h, w)
    result = array.copy()
    result[:, :, 0] = grey
    result[:, :, 1] = grey
    result[:, :, 2] = grey
    _show(result, "Grey")
    return result


def main():
    """Apply every filter to landscape.jpg."""
    try:
        array = ft_load("landscape.jpg")
        if array is None:
            return
        print(array)

        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)

        print(ft_invert.__doc__)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
