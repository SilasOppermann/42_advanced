from give_bmi import give_bmi, apply_limit


def main():
    """Run the subject's example, then a few error cases."""
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


if __name__ == "__main__":
    main()
