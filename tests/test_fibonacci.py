import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.maths.fibonacci import FibonacciCalculator

class TestFibonacciCalculator:
    
    def test_iterative_basic(self):
        """итеративного метод"""
        assert FibonacciCalculator.iterative(0) == 0
        assert FibonacciCalculator.iterative(1) == 1
        assert FibonacciCalculator.iterative(5) == 5
        assert FibonacciCalculator.iterative(10) == 55
    
    def test_recursive_basic(self):
        """рекурсивного метод"""
        assert FibonacciCalculator.recursive(0) == 0
        assert FibonacciCalculator.recursive(1) == 1
        assert FibonacciCalculator.recursive(6) == 8
        assert FibonacciCalculator.recursive(9) == 34
    
    def test_methods_equal(self):
        """итеративный и рекурсивный методы = один результат"""
        for n in range(11):
            iterative = FibonacciCalculator.iterative(n)
            recursive = FibonacciCalculator.recursive(n)
            assert iterative == recursive, f"для n={n}: {iterative} != {recursive}"
    
    def test_sequence_method(self):
        """метод получения последовательности"""
        assert FibonacciCalculator.sequence(0) == []
        assert FibonacciCalculator.sequence(1) == [0]
        assert FibonacciCalculator.sequence(4) == [0, 1, 2, 2]
        assert FibonacciCalculator.sequence(6) == [0, 1, 2, 2, 3, 5]
    
    def test_negative_number(self):
        """отрицательное число"""
        with pytest.raises(ValueError, match="отрицательный индекс"):
            FibonacciCalculator.iterative(-5)
        
        with pytest.raises(ValueError):
            FibonacciCalculator.recursive(-3)

