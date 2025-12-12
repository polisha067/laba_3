class BubbleSort:
    """
    пузырьковая сортировка
    """

    @staticmethod
    def sort(numbers: list[int]) -> list[int]:
        """
        азгумент - numbers(числа для сортировки)
        выход - отсортированный список
        """

        sorted_numbers = numbers.copy()
        length = len(sorted_numbers)

        for i in range(length):
            swap = False

        for j in range(0, length - i - 1):
            if sorted_numbers[j] > sorted_numbers[j+1]:
                sorted_numbers[j], sorted_numbers[j+1] = sorted_numbers[j+1], sorted_numbers[j]
                swap = True

                if not swap:
                    break

            return sorted_numbers
        

    @staticmethod
    def sort_last(numbers: list[int]) -> None:

        length = len(numbers)

        for i in range(length):
            swap = False

            for j in range(0, length - i -1):
                if numbers[j] > numbers[j+1]:
                    numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
                    swap = True

            if not swap:
                break