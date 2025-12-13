
import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.maths.factorial import FactorialCalculator

class TestFactorialCalculator:
    
    def test_iterative_basic(self):
        """итеративного метод"""
        assert FactorialCalculator.iterative(0) == 1
        assert FactorialCalculator.iterative(1) == 1
        assert FactorialCalculator.iterative(4) == 24
        assert FactorialCalculator.iterative(6) == 720
    
    def test_recursive_basic(self):
        """рекурсивного метод"""
        assert FactorialCalculator.recursive(0) == 1
        assert FactorialCalculator.recursive(1) == 1
        assert FactorialCalculator.recursive(4) == 24
        assert FactorialCalculator.recursive(6) == 720
    
    def test_methods_equal(self):
        """итеративный и рекурсивный методы = один результат"""
        for n in range(10):
            iterative = FactorialCalculator.iterative(n)
            recursive = FactorialCalculator.recursive(n)
            assert iterative == recursive, f"Для n={n}: {iterative} != {recursive}"
    
    def test_calculate_method(self):
        """универсальный метод calculate."""
        assert FactorialCalculator.calculate(4, 'iterative') == 24
        assert FactorialCalculator.calculate(6, 'recursive') == 720
        assert FactorialCalculator.calculate(5) == 120 
    
    def test_negative_number(self):

        with pytest.raises(ValueError, match="факториал отрицательного числа"):
            FactorialCalculator.iterative(-10)
        
        with pytest.raises(ValueError):
            FactorialCalculator.recursive(-20)
    
    def test_invalid_method(self):

        with pytest.raises(ValueError, match="такого метода нет"):
            FactorialCalculator.calculate(4, 'неправильный метод')
