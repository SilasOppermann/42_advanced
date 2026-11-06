import sys
from ft_filter import ft_filter


def filter_words(s, n):
    """Return words from s whose length is strictly greater than n."""
    return ft_filter(lambda w: len(w) > n, [w for w in s.split(' ')])


def main():
    """Main function to parse arguments and print filtered word list."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        s = sys.argv[1]
        assert isinstance(s, str), "the arguments are bad"
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        print(filter_words(s, n))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
