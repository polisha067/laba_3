import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.structures.stack import Stack

class TestStack:
    
    def test_initialization(self):
        """инициализация стека"""
        stack = Stack()
        assert stack.is_empty()
        assert stack.size() == 0
    
    def test_push_and_size(self):
        """добавление элементов и размер"""
        stack = Stack()
        stack.push(10)
        assert not stack.is_empty()
        assert stack.size() == 1
        
        stack.push(20)
        stack.push(30)
        assert stack.size() == 3
    
    def test_pop_basic(self):
        """базовое удаление элементов"""
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        
        assert stack.pop() == 30
        assert stack.size() == 2
        assert stack.pop() == 20
        assert stack.pop() == 10
        assert stack.is_empty()
    
    def test_peek(self):
        """просмотр верхнего элемента"""
        stack = Stack()
        stack.push(10)
        assert stack.peek() == 10
        assert stack.size() == 1
        
        stack.push(20)
        assert stack.peek() == 20
        assert stack.size() == 2
        
        stack.push(30)
        assert stack.peek() == 30
        assert stack.size() == 3
    
    def test_pop_empty_stack(self):
        """удаление из пустого стека"""
        stack = Stack()
        
        with pytest.raises(IndexError, match="стек пуст"):
            stack.pop()
    
    def test_peek_empty_stack(self):
        """просмотр пустого стека"""
        stack = Stack()
        
        with pytest.raises(IndexError, match="стек пустой"):
            stack.peek()
    
    def test_multiple_operations(self):
        """несколько операций"""
        stack = Stack()
        
        for i in range(5):
            stack.push(i)
            assert stack.peek() == i
            assert stack.size() == i + 1
        
        for i in range(4, -1, -1):
            assert stack.pop() == i
            assert stack.size() == i