import sys
import string


def count_characters(text):
    """Count upper, lower, punctuation, digit, and space characters."""
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punct = sum(1 for c in text if c in string.punctuation)
    spaces = sum(1 for c in text if c in ' \n')
    digits = sum(1 for c in text if c.isdigit())
    return upper, lower, punct, spaces, digits


def display_counts(text):
    """Display character counts for the given text."""
    upper, lower, punct, spaces, digits = count_characters(text)
    total = len(text)
    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """Main function to handle argument parsing and execution."""
    try:
        assert len(sys.argv) <= 2, "more than one argument provided"
        if len(sys.argv) == 1:
            print("What is the text to count?")
            text = sys.stdin.readline()
        else:
            text = sys.argv[1]
        display_counts(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
