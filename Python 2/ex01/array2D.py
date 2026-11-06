import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Print the shape of a 2D list, then return family[start:end].

    The input must be a non-empty list of lists that all have the same
    length (a "rectangular" 2D array). On error, prints a message and
    returns an empty list.
    """
    try:
        if not isinstance(family, list) or len(family) == 0:
            raise TypeError("family must be a non-empty list")
        if not all(isinstance(row, list) for row in family):
            raise TypeError("family must be a list of lists (2D)")
        # Every row must have the same length as the first one,
        # otherwise it is not a valid 2D array (it would be "jagged").
        if any(len(row) != len(family[0]) for row in family):
            raise ValueError("all rows must have the same size")
        if (isinstance(start, bool) or isinstance(end, bool)
                or not isinstance(start, int) or not isinstance(end, int)):
            raise TypeError("start and end must be integers")

        # np.array(...).shape gives (number_of_rows, number_of_columns)
        print(f"My shape is : {np.array(family).shape}")

        # Slicing: [start:end] keeps rows from index `start` up to, but
        # NOT including, `end`. Negative indexes count from the end:
        # with 4 rows, -2 means index 2, so [1:-2] keeps only row 1.
        new_family = family[start:end]

        print(f"My new shape is : {np.array(new_family).shape}")
        return new_family
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
        return []


def main():
    """Nothing to run: this file is a module meant to be imported."""
    pass


if __name__ == "__main__":
    main()
