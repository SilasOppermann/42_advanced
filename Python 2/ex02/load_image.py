import numpy as np
from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> np.ndarray:
    """Load a JPG/JPEG image, print its shape, return it as an RGB array."""
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")

        # with closes file after process
        with Image.open(path) as img:
            # img.format check,t actual file content not ending
            if img.format not in ("JPEG", "JPG"):
                raise ValueError(f"unsupported format '{img.format}', "
                                 "only JPG/JPEG are accepted")
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
    """Run sample and error cases."""
    print(ft_load("landscape.jpg"))

    print("--- error cases ---")
    print(ft_load("does_not_exist.jpg"))
    print(ft_load("load_image.py"))     # exists but is not an image
    print(ft_load(42))                  # not a string


if __name__ == "__main__":
    main()
