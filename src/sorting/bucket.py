class BucketSort:
    """
    класс блочной сортировки.
    """

    @staticmethod
    def sort(numbers: list[float], buckets_count: int | None = None) -> list[float]:
        """
        блочная сортировка для чисел в диапазоне [0, 1).

        numbers - Список чисел с плавающей точкой в диапазоне [0, 1)
        выход - тсортированный список
        """
        if not numbers:
            return []
        
        #
        if buckets_count is None:
            buckets_count = len(numbers)
        
        
        buckets = [[] for _ in range(buckets_count)]
        
        
        for number in numbers:
            if number < 0 or number >= 1:
                
                min_val = min(numbers)
                max_val = max(numbers)
                if max_val == min_val:
                    normalized = 0.0
                else:
                    normalized = (number - min_val) / (max_val - min_val)
                bucket_index = int(normalized * buckets_count)
            else:
                bucket_index = int(number * buckets_count)
            
            
            if bucket_index == buckets_count:
                bucket_index = buckets_count - 1
            
            buckets[bucket_index].append(number)
        
        for i in range(buckets_count):
            buckets[i].sort()  
        
        
        sorted_numbers = []
        for bucket in buckets:
            sorted_numbers.extend(bucket)
        
        return sorted_numbers
    
    @staticmethod
    def sort_with_insertion(numbers: list[float]) -> list[float]:
        """
        блочная сортировка с использованием сортировки вставками внутри блоков.
        """
        if not numbers:
            return []
        
        buckets_count = len(numbers)
        buckets = [[] for _ in range(buckets_count)]
        
        
        for number in numbers:
            
            min_val = min(numbers)
            max_val = max(numbers)
            if max_val == min_val:
                normalized = 0.0
            else:
                normalized = (number - min_val) / (max_val - min_val)
            
            bucket_index = int(normalized * buckets_count)
            if bucket_index == buckets_count:
                bucket_index = buckets_count - 1
            
            buckets[bucket_index].append(number)
        
        
        for bucket in buckets:
            BucketSort._insertion_sort(bucket)
        
        
        sorted_numbers = []
        for bucket in buckets:
            sorted_numbers.extend(bucket)
        
        return sorted_numbers
    
    @staticmethod
    def _insertion_sort(numbers: list[float]) -> None:
        
        for i in range(1, len(numbers)):
            key = numbers[i]
            j = i - 1
            
            while j >= 0 and numbers[j] > key:
                numbers[j + 1] = numbers[j]
                j -= 1
            
            numbers[j + 1] = key