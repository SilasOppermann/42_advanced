import numpy as np


def _check_number_list(values: list, name: str) -> None:
    """Raise an error if `values` is not a list of int/float numbers.

    Small private helper (the leading underscore means "internal use"),
    so both public functions can share the same validation.
    """
    if not isinstance(values, list):
        raise TypeError(f"{name} must be a list")
    for v in values:
        # bool is a subclass of int in Python (True == 1), so we have to
        # reject it explicitly, otherwise [True, 2.0] would be accepted.
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            raise TypeError(f"{name} must only contain int or float")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Return the list of BMI values (weight / height²) for each person.

    Returns an empty list and prints an error message if the input
    is invalid (wrong type, different sizes, non-positive height).
    """
    try:
        _check_number_list(height, "height")
        _check_number_list(weight, "weight")
        if len(height) != len(weight):
            raise ValueError("height and weight must have the same size")

        # Convert the Python lists into numpy arrays. With numpy, math
        # operators work element by element ("vectorized"), so no loop
        # is needed: h ** 2 squares every height at once.
        h = np.array(height, dtype=float)
        w = np.array(weight, dtype=float)
        if np.any(h <= 0):
            raise ValueError("height values must be greater than 0")

        bmi = w / h ** 2
        # .tolist() converts the numpy array back to a normal Python list
        # (the subject expects <class 'list'>, not numpy.ndarray).
        return bmi.tolist()
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list of booleans: True where the BMI is above `limit`."""
    try:
        _check_number_list(bmi, "bmi")
        if isinstance(limit, bool) or not isinstance(limit, (int, float)):
            raise TypeError("limit must be an int or float")

        # Comparing a numpy array with a number gives an array of bools,
        # e.g. np.array([22.5, 29.0]) > 26  ->  array([False, True]).
        return (np.array(bmi, dtype=float) > limit).tolist()
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
        return []


def main():
    """Nothing to run: this file is a module meant to be imported."""
    pass


if __name__ == "__main__":
    main()
