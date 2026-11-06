from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def main():
    """Apply every filter to landscape.jpg (one window each)."""
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


if __name__ == "__main__":
    main()
