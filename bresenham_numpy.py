import numpy as np
from typing import Tuple, Union, List


def bresenham_numpy(
        x0: Union[float, int],
        y0: Union[float, int],
        x1: Union[float, int],
        y1: Union[float, int]
) -> Tuple[np.ndarray, np.ndarray]:
    """Return integer coordinates on the line from (x0, y0) to (x1, y1).

    The result will contain both the start and the end point.

    :param x0: The X coordinate of the first point
    :type x0: float or int
    :param y0: The Y coordinate of the first point
    :type y0: float or int
    :param x1: The X coordinate of the second point
    :type x1: float or int
    :param y1: The Y coordinate of the second point
    :type y1: float or int
    :return: The X and Y integer coordinates on the line from (x0, y0) to (x1, y1)
    :rtype: tuple of two Numpy arrays
    """

    if abs(y1 - y0) > abs(x1 - x0):
        swapped = True
        x0, y0, x1, y1 = y0, x0, y1, x1
    else:
        swapped = False

    m = (y1 - y0) / (x1 - x0) if x1 - x0 != 0 else +1
    q = y0 - m * x0

    if x0 < x1:
        xs = np.arange(np.floor(x0), np.ceil(x1) + 1, +1, dtype=int)
    else:
        xs = np.arange(np.ceil(x0), np.floor(x1) - 1, -1, dtype=int)
    ys = np.round(m * xs + q).astype(int)

    if swapped:
        xs, ys = ys, xs

    return xs, ys

def convert_to_tuples(
        xs: np.ndarray,
        ys: np.ndarray
) -> List[Tuple[int, int]]:
    return [(x, y) for x, y in zip(xs, ys)]