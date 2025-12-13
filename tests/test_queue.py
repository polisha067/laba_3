import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.structures.queue import Queue

class TestQueue:
    
    def test_initialization(self):
        """инициализация очереди"""
        queue = Queue()
        assert queue.is_empty()
        assert queue.size() == 0
    
    def test_enqueue_and_size(self):
        """добавление элементов и размер"""
        queue = Queue()
        queue.enqueue("первый")
        assert not queue.is_empty()
        assert queue.size() == 1
        
        queue.enqueue("второй")
        queue.enqueue("третий")
        assert queue.size() == 3
    
    def test_dequeue_basic(self):
        """базовое удаление элементов"""
        queue = Queue()
        queue.enqueue("Полина")
        queue.enqueue("Петр")
        queue.enqueue("Екатерина")
        queue.enqueue("Наталья")
        
        assert queue.dequeue() == "Полина"
        assert queue.size() == 3
        assert queue.dequeue() == "Петр"
        assert queue.dequeue() == "Екатерина"
        assert queue.dequeue() == "Наталья"
        assert queue.is_empty()
    
    def test_front(self):
        """просмотр первого элемента"""
        queue = Queue()
        queue.enqueue(10)
        assert queue.front() == 10
        assert queue.size() == 1
        
        queue.enqueue(20)
        assert queue.front() == 10
        assert queue.size() == 2
        
        queue.enqueue(30)
        assert queue.front() == 10
        assert queue.size() == 3
    
    def test_dequeue_empty_queue(self):
        """удаление из пустой очереди"""
        queue = Queue()
        
        with pytest.raises(IndexError, match="очередь пустая"):
            queue.dequeue()
    
    def test_front_empty_queue(self):
        """просмотр пустой очереди"""
        queue = Queue()
        
        with pytest.raises(IndexError, match="очередь пустая"):
            queue.front()
    
    def test_fifo_order(self):
        """принцип fifo"""
        queue = Queue()
        
        elements = [1, 2, 3, 4, 5, 6, 7]
        for elem in elements:
            queue.enqueue(elem)
        
        for elem in elements:
            assert queue.dequeue() == elem
    
    def test_multiple_operations(self):
        """несколько операций"""
        queue = Queue()
        
        queue.enqueue(1)
        assert queue.front() == 1
        
        queue.enqueue(2)
        assert queue.front() == 1
        
        assert queue.dequeue() == 1
        assert queue.front() == 2
        
        queue.enqueue(3)
        queue.enqueue(4)
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.dequeue() == 4
        assert queue.is_empty()