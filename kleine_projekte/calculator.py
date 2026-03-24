"""Kleines Projekt 1: Taschenrechner (Calculator).

A simple calculator supporting basic arithmetic operations.
"""


class Calculator:
    """A simple calculator for basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Return the sum of *a* and *b*."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Return the difference of *a* minus *b*."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Return the product of *a* and *b*."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Return the quotient of *a* divided by *b*.

        Raises:
            ValueError: If *b* is zero.
        """
        if b == 0:
            raise ValueError("Division durch Null ist nicht erlaubt.")
        return a / b
