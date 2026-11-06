import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_transpose(matrix: np.ndarray) -> np.ndarray:
    """Return the transpose of a 2D array, done by hand (no library).

    Transposing swaps rows and columns: the value at [row][col] moves
    to [col][row]. So the first row becomes the first column, etc.
    Visually that is a mirror along the top-left -> bottom-right diagonal.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    # The result has the opposite shape: (cols, rows).
    result = np.zeros((cols, rows), dtype=matrix.dtype)
    for r in range(rows):
        for c in range(cols):
            result[c][r] = matrix[r][c]
    return result


def main():
    """Load animal.jpeg, cut a square, transpose it and display it."""
    try:
        image = ft_load("animal.jpeg")
        if image is None:
            return

        # Same square + single channel as in ex03 -> shape (400, 400, 1)
        square = image[100:500, 450:850, 0:1]
        print(f"The shape of image is: {square.shape}")
        print(square)

        # Our transpose works on 2D, so drop the last axis: (400, 400)
        transposed = ft_transpose(square[:, :, 0])
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        plt.imshow(transposed, cmap="gray")
        plt.show()
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
