import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.sorting.bubble import BubbleSort

class TestBubbleSort:
    
    def test_empty_array(self):
        """пустой массив"""
        sorter = BubbleSort()
        assert sorter.sort([]) == []
    
    def test_single_element(self):
        """массив из одного элемента"""
        sorter = BubbleSort()
        assert sorter.sort([42]) == [42]
    
    def test_already_sorted(self):
        """уже отсортированный массив"""
        sorter = BubbleSort()
        arr = [1, 2, 3, 4, 5]
        assert sorter.sort(arr.copy()) == arr
    
    def test_reverse_sorted(self):
        """обратно отсортированный массив"""
        sorter = BubbleSort()
        arr = [5, 4, 3, 2, 1]
        assert sorter.sort(arr.copy()) == [1, 2, 3, 4, 5]
    
    def test_random_array(self):
        """случайный массив"""
        sorter = BubbleSort()
        arr = [45, 35, 25, 15, 55, 11, 99]
        expected = sorted(arr)
        assert sorter.sort(arr.copy()) == expected
    
    def test_with_duplicates(self):
        """массив с дубликатами"""
        sorter = BubbleSort()
        arr = [3, 5, 4, 3, 5, 4, 1]
        expected = sorted(arr)
        assert sorter.sort(arr.copy()) == expected
    
    def test_sort_inplace(self):
        """сортировка на месте"""
        sorter = BubbleSort()
        arr = [5, 3, 4, 1, 2]
        sorter.sort_inplace(arr)
        assert arr == [1, 2, 3, 4, 5]