from .counting import CountingSort
class RadixSort:
    """
    класс для поразрядной сортировки.
    """

    @staticmethod
    def sort(numbers: list[int], base: int = 10) -> list[int]:
        """
        поразрядная сортировка.

        numbers - список неотрицательных целых чисел
        выход - отсортированный список
        """
        if not numbers:
            return []
        
        # Проверяем, что все числа неотрицательные
        if any(num < 0 for num in numbers):
            raise ValueError("только с неотрицательными числами")
        
        numbers_copy = numbers.copy()
        
        
        max_number = max(numbers_copy)
        
        
        digit_place = 1
        while max_number // digit_place > 0:
            numbers_copy = CountingSort.sort_for_digits(numbers_copy, digit_place)
            digit_place *= base
        
        return numbers_copy