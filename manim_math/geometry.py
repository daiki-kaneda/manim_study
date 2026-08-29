"""Geometry helpers shared by short math videos."""

from __future__ import annotations


def staircase_cells(n: int) -> list[tuple[int, int]]:
    """Grid coordinates (col, row) for 1 + 2 + ... + n, row 0 at the top."""
    cells: list[tuple[int, int]] = []
    for row in range(n):
        for col in range(row + 1):
            cells.append((col, row))
    return cells


def rectangle_cells(rows: int, cols: int) -> list[tuple[int, int]]:
    return [(c, r) for r in range(rows) for c in range(cols)]


def odd_layer_cells(k: int) -> list[tuple[int, int]]:
    """Cells for the k-th odd number as an L around a (k-1)×(k-1) square.

    k starts at 1 (a single cell). Coordinates have origin at the bottom-left
    of the finished n×n square.
    """
    if k < 1:
        raise ValueError("k must be >= 1")
    if k == 1:
        return [(0, 0)]
    cells = [(k - 1, y) for y in range(k)]
    cells.extend((x, k - 1) for x in range(k - 1))
    return cells


def polar(radius: float, angle: float) -> tuple[float, float, float]:
    """Return a 3D point at the given polar angle (radians), z=0."""
    from math import cos, sin

    return (radius * cos(angle), radius * sin(angle), 0.0)
