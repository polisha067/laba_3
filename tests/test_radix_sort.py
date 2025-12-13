import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.sorting.radix import RadixSort

class TestRadixSort:
    
    def test_empty_array(self):
        """пустой массив"""
        sorter = RadixSort()
        assert sorter.sort([]) == []
    
    def test_single_element(self):
        """массив из одного элемента"""
        sorter = RadixSort()
        assert sorter.sort([8]) == [8]
    
    def test_basic_sorting(self):
        """базовая сортировка"""
        sorter = RadixSort()
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        expected = sorted(arr)
        assert sorter.sort(arr.copy()) == expected
    
    def test_small_numbers(self):
        """маленькие числа"""
        sorter = RadixSort()
        arr = [5, 3, 8, 1, 7, 2, 6]
        expected = sorted(arr)
        assert sorter.sort(arr.copy()) == expected
    
    def test_medium_numbers(self):
        """средние числа"""
        sorter = RadixSort()
        arr = [123, 456, 789, 234, 567, 891]
        expected = sorted(arr)
        assert sorter.sort(arr.copy()) == expected
    
    def test_with_duplicates(self):
        """массив с дубликатами"""
        sorter = RadixSort()
        arr = [121, 432, 121, 564, 432, 121]
        expected = sorted(arr)
        assert sorter.sort(arr.copy()) == expected
    
    def test_negative_numbers_error(self):
        """отрицательные числа - ошибка"""
        sorter = RadixSort()
        arr = [5, -1, 3, -2]
        
        with pytest.raises(ValueError, match="неотрицательными"):
            sorter.sort(arr)