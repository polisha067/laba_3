class CountingSort:
    """
    класс для сортировки подсчетом.
    """

    @staticmethod
    def sort(numbers: list[int]) -> list[int]:
        """
        сортировка подсчетом.

        numbers - список целых неотрицательных чисел
        выход - отсортированный список

        """
        if not numbers:
            return []

        if any(num < 0 for num in numbers):
            raise ValueError("только с неотрицательными числами")
        
        min_value = min(numbers)
        max_value = max(numbers)

        count_size = max_value - min_value + 1
        count = [0] * count_size

        for number in numbers:
            count[number - min_value] += 1

        sorted_numbers = []
        for i in range(count_size):
            sorted_numbers.extend([i + min_value] * count[i])
        
        return sorted_numbers
    
    @staticmethod
    def sort_for_digits(numbers: list[int], digit_place: int) -> list[int]:
        """
        сортировка подсчетом для конкретного разряда (для Radix Sort).
        
        numbers - список чисел
        выход - отсортированный по разряду список
        """
        count_size = 10  
        count = [0] * count_size

        for number in numbers:
            digit = (number // digit_place) % 10
            count[digit] += 1

        for i in range(1, count_size):
            count[i] += count[i - 1]

        sorted_numbers = [0] * len(numbers)

        for i in range(len(numbers) - 1, -1, -1):
            digit = (numbers[i] // digit_place) % 10
            position = count[digit] - 1
            sorted_numbers[position] = numbers[i]
            count[digit] -= 1
        
        return sorted_numbers