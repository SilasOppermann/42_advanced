from array2D import slice_me


def main():
    """Run the subject's example, then a few error cases."""
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

    print("--- error cases ---")
    print(slice_me("not a list", 0, 2))
    print(slice_me([[1, 2], [3]], 0, 1))        # rows of different size
    print(slice_me([1, 2, 3], 0, 1))            # 1D, not 2D
    print(slice_me(family, "0", 2))             # bad index type


if __name__ == "__main__":
    main()
