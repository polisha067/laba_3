class HeapSort:
    """
    класс для пирамидальной сортировки.
    """

    @staticmethod
    def sort(numbers: list[int]) -> list[int]:
        """
        пирамидальная сортировка.
 
        numbers - список чисел для сортировки
        выход - отсортированный список
        """
        numbers_copy = numbers.copy()
        HeapSort._heap_sort(numbers_copy)
        return numbers_copy
    
    @staticmethod
    def sort_inplace(numbers: list[int]) -> None:

        HeapSort._heap_sort(numbers)
    
    @staticmethod
    def _heap_sort(numbers: list[int]) -> None:

        length = len(numbers)
        

        for i in range(length // 2 - 1, -1, -1):
            HeapSort._heapify(numbers, length, i)
        

        for i in range(length - 1, 0, -1):
            numbers[0], numbers[i] = numbers[i], numbers[0]  
            HeapSort._heapify(numbers, i, 0)  
    
    @staticmethod
    def _heapify(numbers: list[int], heap_size: int, root_index: int) -> None:
        """
        преобразование поддерева в max-кучу.

            numbers - список чисел
            heap_size - размер кучи
            root_index - индекс корня поддерева
        """
        largest = root_index
        left_child = 2 * root_index + 1
        right_child = 2 * root_index + 2
        

        if left_child < heap_size and numbers[left_child] > numbers[largest]:
            largest = left_child
        

        if right_child < heap_size and numbers[right_child] > numbers[largest]:
            largest = right_child
        

        if largest != root_index:
            numbers[root_index], numbers[largest] = numbers[largest], numbers[root_index]

            HeapSort._heapify(numbers, heap_size, largest)