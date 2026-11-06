import numpy as np
from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> np.ndarray:
    """Load a JPG/JPEG image and return its pixels as an RGB numpy array.

    The array has the shape (height, width, 3): one row per pixel line,
    one column per pixel, and 3 values (Red, Green, Blue, 0-255) per
    pixel. Prints the shape. Returns None (with a clear message) if the
    image cannot be loaded.
    """
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")

        # "with" makes sure the file is closed after we are done with it.
        with Image.open(path) as img:
            # img.format is detected from the file content, not from the
            # extension, so a .png renamed to .jpg is still refused.
            if img.format not in ("JPEG", "JPG"):
                raise ValueError(f"unsupported format '{img.format}', "
                                 "only JPG/JPEG are accepted")
            # convert("RGB") guarantees 3 channels, even if the file is
            # grayscale or CMYK. np.array turns the image into numbers.
            array = np.array(img.convert("RGB"))

        print(f"The shape of image is: {array.shape}")
        return array
    except FileNotFoundError:
        print(f"Error: file '{path}' not found")
    except UnidentifiedImageError:
        print(f"Error: '{path}' is not a valid image")
    except (TypeError, ValueError, OSError) as error:
        print(f"Error: {error}")
    return None


def main():
    """Nothing to run: this file is a module meant to be imported."""
    pass


if __name__ == "__main__":
    main()
