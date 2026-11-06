import numpy as np


def _check_number_list(values: list, name: str) -> None:
    """Raise TypeError unless values is a list of int/float."""
    if not isinstance(values, list):
        raise TypeError(f"{name}-List must be a list, DUH!")
    for v in values:
        # bool is a subclass of int in Python -> have to reject it explicitly
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            raise TypeError(f"{name}-List must only contain int or float")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Return the BMI for each height/weight pair."""
    try:
        _check_number_list(height, "height")
        _check_number_list(weight, "weight")
        if len(height) != len(weight):
            raise ValueError("Lists are not the same Length")
        # numpy vectorizes the list, so operations apply to all
        # elements at once without  for loop
        h = np.array(height, dtype=float)
        w = np.array(weight, dtype=float)
        if np.any((h <= 0) | (w <= 0)):
            raise ValueError("height and weight values must be greater than 0")

        bmi = w / h ** 2  # this is a vector now
        return bmi.tolist()
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return True for each BMI above limit, else False."""
    try:
        _check_number_list(bmi, "bmi")
        if isinstance(limit, bool) or not isinstance(limit, (int, float)):
            raise TypeError("limit must be an int or float")
        return (np.array(bmi, dtype=float) > limit).tolist()
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
        return []


def main():
    """Run sample and error cases."""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    print("--- error cases ---")
    print(give_bmi([1.8, 1.7], [80]))          # different sizes
    print(give_bmi([1.8, "a"], [80, 70]))      # not a number
    print(give_bmi("hello", [80]))             # not a list
    print(give_bmi([0, 1.7], [80, 70]))        # height 0 -> /0
    print(apply_limit([20, 30], "26"))         # bad limit
    return


if __name__ == "__main__":
    main()
