import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.sorting.bucket import BucketSort

class TestBucketSort:
    
    def test_empty_array(self):
        """пустой массив"""
        sorter = BucketSort()
        assert sorter.sort([]) == []
    
    def test_single_element(self):
        """массив из одного элемента"""
        sorter = BucketSort()
        assert sorter.sort([0.5]) == [0.5]
    
    def test_basic_float_sorting(self):
        """базовая сортировка float"""
        sorter = BucketSort()
        arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21]
        expected = sorted(arr)
        result = sorter.sort(arr.copy())
        
        for r, e in zip(result, expected):
            assert abs(r - e) < 0.0001
    
    def test_integer_as_float(self):
        """целые числа как float"""
        sorter = BucketSort()
        arr = [5, 3, 8, 1, 7, 2, 6]
        expected = sorted(arr)
        result = sorter.sort([float(x) for x in arr])
        
        result_int = [int(x) for x in result]
        assert result_int == expected
    
    def test_values_outside_0_1(self):
        """числа вне диапазона [0,1)"""
        sorter = BucketSort()
        arr = [5.0, 1.0, 3.0, 2.0, 4.0, 7.0, 6.0]
        expected = sorted(arr)
        result = sorter.sort(arr.copy())
        
        for r, e in zip(result, expected):
            assert abs(r - e) < 0.0001
    
    def test_all_same_values(self):
        """все значения одинаковые"""
        sorter = BucketSort()
        arr = [0.5, 0.5, 0.5, 0.5, 0.5]
        assert sorter.sort(arr.copy()) == arr
    
    def test_mixed_values(self):
        """смешанные значения"""
        sorter = BucketSort()
        arr = [0.1, 0.9, 0.2, 0.8, 0.3, 0.7, 0.4, 0.6]
        expected = sorted(arr)
        result = sorter.sort(arr.copy())
        
        for r, e in zip(result, expected):
            assert abs(r - e) < 0.0001