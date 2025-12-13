class Queue:
    """
    реализация очереди.
    """
    def __init__(self):
        self._data = []
    
    def enqueue(self, item): # + в конец очереди
        self._data.append(item)
    
    def dequeue(self): # удалить и вернуть элемент из начала очереди
        if self.is_empty():
            raise IndexError("пустая очередь")
        return self._data.pop(0)
    
    def front(self): # посмотреть первый элемент без удаления
        if self.is_empty():
            raise IndexError("пустая очередь")
        return self._data[0]

    def is_empty(self): # проверка на пустоту
        return len(self._data) == 0
    
    def size(self): # размер очереди
        return len(self._data)