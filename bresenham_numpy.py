import numpy as np
from typing import Tuple, Union


def bresenham(
        x0: Union[float, int],
        y0: Union[float, int],
        x1: Union[float, int],
        y1: Union[float, int]
) -> Tuple[np.ndarray, np.ndarray]:
    """Return integer coordinates on the line from (x0, y0) to (x1, y1).

    The result will contain both the start and the end point.

    :param x0: The X coordinate of the first point
    :param y0: The Y coordinate of the first point
    :param x1: The X coordinate of the second point
    :param y1: The Y coordinate of the second point
    :return: The X and Y integer coordinates on the line from (x0, y0) to (x1, y1)
    """

    m = (y1 - y0) / (x1 - x0)
    q = y0 - m * x0

    if abs(m) > 1:
        swapped = True
        m, q = 1 / m, -q / m
        x0, y0, x1, y1 = y0, x0, y1, x1
    else:
        swapped = False

    step = +1 if x0 < x1 else -1
    xs = np.arange(np.floor(x0), np.ceil(x1) + step, step, dtype=int)
    ys = np.round(m * xs + q).astype(int)

    if swapped:
        xs, ys = ys, xs

    return xs, ys
