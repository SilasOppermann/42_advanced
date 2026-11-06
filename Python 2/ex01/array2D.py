import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Print the shape of family and return family[start:end]."""
    try:
        if not isinstance(family, list) or len(family) == 0:
            raise TypeError("lsit must be a non-empty ")
        if not all(isinstance(row, list) for row in family):
            raise TypeError("lsit must be 2D")
        if any(len(row) != len(family[0]) for row in family):
            raise ValueError("all rows must have the same size")
        if (isinstance(start, bool) or isinstance(end, bool)
                or not isinstance(start, int) or not isinstance(end, int)):
            raise TypeError("start and end must be integers")

        print(f"My shape is : {np.array(family).shape}")
        new_family = family[start:end]

        print(f"My new shape is : {np.array(new_family).shape}")
        return new_family
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
        return []


def main():
    """Run sample and error cases."""
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
    return


if __name__ == "__main__":
    main()
