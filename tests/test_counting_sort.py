import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.sorting.counting import CountingSort

class TestCountingSort:
    
    def test_empty_array(self):
        """пустой массив"""
        sorter = CountingSort()
        assert sorter.sort([]) == []
    
    def test_single_element(self):
        """массив из одного элемента"""
        sorter = CountingSort()
        assert sorter.sort([7]) == [7]
    
    def test_basic_sorting(self):
        """базовая сортировка"""
        sorter = CountingSort()
        arr = [4, 2, 7, 1, 3, 6, 5]
        expected = sorted(arr)
        assert sorter.sort(arr.copy()) == expected
    
    def test_with_duplicates(self):
        """массив с дубликатами"""
        sorter = CountingSort()
        arr = [3, 1, 3, 2, 1, 2, 3]
        expected = sorted(arr)
        assert sorter.sort(arr.copy()) == expected
    
    def test_small_range(self):
        """маленький диапазон чисел"""
        sorter = CountingSort()
        arr = [1, 0, 1, 0, 1, 0, 1]
        expected = sorted(arr)
        assert sorter.sort(arr.copy()) == expected
    
    def test_all_same_elements(self):
        """все элементы одинаковые"""
        sorter = CountingSort()
        arr = [5, 5, 5, 5, 5]
        assert sorter.sort(arr.copy()) == arr
    
    def test_negative_numbers_error(self):
        """отрицательные числа - ошибка"""
        sorter = CountingSort()
        arr = [5, -1, 3, -2]
        
        with pytest.raises(ValueError, match="неотрицательными"):
            sorter.sort(arr)