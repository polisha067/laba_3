class QuickSort:


    @staticmethod
    def sort(numbers: list[int]) -> list[int]:
        """
        быстрая сортировка (рекурсивная).
        numbers - cписок чисел для сортировки
        выход: отсортированный список
        """
        if len(numbers) <= 1:
            return numbers.copy()
        
        pivot = numbers[len(numbers) // 2]

        left = [x for x in numbers if x < pivot]
        middle = [x for x in numbers if x == pivot]
        right = [x for x in numbers if x > pivot]
        
        return QuickSort.sort(left) + middle + QuickSort.sort(right)
    

    @staticmethod
    def sort_inplace(numbers: list[int]) -> None:

        QuickSort._quick_sort_helper(numbers, 0, len(numbers) - 1)
    


    @staticmethod
    def _quick_sort_helper(numbers: list[int], low: int, high: int) -> None:
        """
            numbers - cписок чисел
            low - нижний индекс
            high - верхний индекс
        """
        if low < high:
            
            partition_index = QuickSort._partition(numbers, low, high)
            
           
            QuickSort._quick_sort_helper(numbers, low, partition_index - 1)
            QuickSort._quick_sort_helper(numbers, partition_index + 1, high)
    
    @staticmethod
    def _partition(numbers: list[int], low: int, high: int) -> int:

        pivot = numbers[high]

        i = low - 1
        
        for j in range(low, high):
            if numbers[j] <= pivot:
                i += 1
                numbers[i], numbers[j] = numbers[j], numbers[i]
        
        numbers[i + 1], numbers[high] = numbers[high], numbers[i + 1]
        return i + 1