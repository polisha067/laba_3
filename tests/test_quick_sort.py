import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.sorting.quick import QuickSort

class TestQuickSort:
    
    def test_empty_array(self):
        """пустой массив"""
        sorter = QuickSort()
        assert sorter.sort([]) == []
    
    def test_single_element(self):
        """массив из одного элемента"""
        sorter = QuickSort()
        assert sorter.sort([42]) == [42]
    
    def test_small_array(self):
        """небольшой массив"""
        sorter = QuickSort()
        arr = [5, 4, 3, 1, 2]
        assert sorter.sort(arr.copy()) == [1, 2, 3, 4, 5]
    
    def test_with_duplicates(self):
        """массив с дубликатами"""
        sorter = QuickSort()
        arr = [2, 1, 3, 1, 5, 2, 9, 3, 5, 6]
        expected = sorted(arr)
        assert sorter.sort(arr.copy()) == expected
    
    def test_sort_inplace(self):
        """сортировка на месте"""
        sorter = QuickSort()
        arr = [5, 3, 4, 1, 2]
        sorter.sort_inplace(arr)
        assert arr == [1, 2, 3, 4, 5]