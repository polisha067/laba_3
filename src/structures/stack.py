class Stack:
    """
    реализация стека
    """
    def __init__(self):
        self._data = []
    
    def push(self, item): # добавить элемент на вершину стека
        self._data.append(item)
    
    def pop(self): # удалить и вернуть элемент с вершины стека
        if self.is_empty():
            raise IndexError("cтек пустjq")
        return self._data.pop()
    
    def peek(self): # посмотреть верхний элемент без удаления
        if self.is_empty():
            raise IndexError("стек пустой")
        return self._data[-1]
    
    def is_empty(self): # проверка на пустоту
        return len(self._data) == 0
    
    def size(self): # размер стека
        return len(self._data)