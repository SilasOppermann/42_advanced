from load_image import ft_load


def main():
    """Run the subject's example, then a few error cases."""
    print(ft_load("landscape.jpg"))

    print("--- error cases ---")
    print(ft_load("does_not_exist.jpg"))
    print(ft_load("tester.py"))       # exists but is not an image
    print(ft_load(42))                # not a string


if __name__ == "__main__":
    main()
