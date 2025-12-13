import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.sorting.heap import HeapSort

class TestHeapSort:
    
    def test_empty_array(self):
        """пустой массив"""
        sorter = HeapSort()
        assert sorter.sort([]) == []
    
    def test_single_element(self):
        """массив из одного элемента"""
        sorter = HeapSort()
        assert sorter.sort([8]) == [8]
    
    def test_basic_sorting(self):
        """базовая сортировка"""
        sorter = HeapSort()
        arr = [4, 10, 3, 5, 1, 7, 6]
        expected = sorted(arr)
        assert sorter.sort(arr.copy()) == expected
    
    def test_with_negative_numbers(self):
        """массив с отрицательными числами"""
        sorter = HeapSort()
        arr = [-5, -1, -3, 0, 2, -2, 4]
        expected = sorted(arr)
        assert sorter.sort(arr.copy()) == expected
    
    def test_already_sorted(self):
        """уже отсортированный массив"""
        sorter = HeapSort()
        arr = [1, 2, 3, 4, 5, 6, 7]
        expected = sorted(arr)
        assert sorter.sort(arr.copy()) == expected
    
    def test_reverse_sorted(self):
        """обратно отсортированный массив"""
        sorter = HeapSort()
        arr = [7, 6, 5, 4, 3, 2, 1]
        expected = sorted(arr)
        assert sorter.sort(arr.copy()) == expected
    
    def test_sort_inplace(self):
        """сортировка на месте"""
        sorter = HeapSort()
        arr = [5, 3, 8, 1, 7, 2, 6]
        sorter.sort_inplace(arr)
        assert arr == [1, 2, 3, 5, 6, 7, 8]