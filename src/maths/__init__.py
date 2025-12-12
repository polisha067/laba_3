"""
пакет с математическими утилитами: факториал и числа фибоначчи.
"""

from .factorial import FactorialCalculator
from .fibonacci import FibonacciCalculator, fibonacci, fibonacci_recursive

__all__ = [
    
    "FactorialCalculator",
    "FibonacciCalculator",

]

