import os


def ft_tqdm(lst: range) -> None:
    """Mimic the tqdm progress bar using the yield operator."""
    total = len(lst)
    term_width = os.get_terminal_size().columns
    suffix_max = f"| {total}/{total}"
    prefix = "100%|["
    bar_width = term_width - len(prefix) - len(suffix_max) - 1
    if bar_width < 1:
        bar_width = 1

    for i, elem in enumerate(lst):
        yield elem
        current = i + 1
        percent = int(100 * current / total)
        filled = int(bar_width * current / total)
        if current >= total:
            bar = "=" * bar_width
        elif filled > 0:
            bar = "=" * (filled - 1) + ">" + " " * (bar_width - filled)
        else:
            bar = " " * bar_width
        suffix = f"| {current}/{total}"
        print(
            f"\r{percent}%|[{bar}]{suffix}",
            end="",
            flush=True,
        )


def main():
    """Entry point — no action when run directly."""
    pass


if __name__ == "__main__":
    main()
