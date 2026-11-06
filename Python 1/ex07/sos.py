import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
    "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ",
    "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
    "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
    "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
    "Y": "-.-- ", "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
    "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
    "8": "---.. ", "9": "----. ",
}


def encode_morse(text):
    """Encode a string of alphanumeric and space characters into Morse code."""
    return "".join(NESTED_MORSE[c] for c in text.upper()).rstrip()


def main():
    """Main function to validate arguments and print Morse encoding."""
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        text = sys.argv[1]
        assert isinstance(text, str), "the arguments are bad"
        assert all(
            c.upper() in NESTED_MORSE for c in text
        ), "the arguments are bad"
        print(encode_morse(text))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
