"""
пакет с математическими утилитами: факториал и числа фибоначчи.
"""

from .factorial import FactorialCalculator, factorial, factorial_recursive
from .fibonacci import FibonacciCalculator, fibonacci, fibonacci_recursive

__all__ = [
    "FactorialCalculator",
    "FibonacciCalculator",
    "factorial",
    "factorial_recursive",
    "fibonacci",
    "fibonacci_recursive",
]

