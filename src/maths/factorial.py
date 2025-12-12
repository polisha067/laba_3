
class FactorialCalculator:
    """
    класс для вычисления факториалов.
    """

    @staticmethod
    def iterative(number: int) -> int:
        """
        итеративно вычислить факториал.
        """
        if number < 0:
            raise ValueError("факториал отрицательного числа")
        result = 1

        for i in range(1, number+1):
            result *= i
        return result


    @staticmethod
    def recursive(number: int) -> int:
        """
        рекурсивно вычислить факториал.
        """
        if number < 0:
            raise ValueError("факториал отрицательного числа")
        
        if number == 0:
            return 1
        return number * FactorialCalculator.recursive(number - 1)


@classmethod
def calculate(cls, number: int, method: str = 'iterative') -> int:
    """
    вычисление фаакториала
    """
    if method == 'iterative':
        return cls.iterative(number)
    elif method == 'recursive':
        return cls.recursive(number)
    else:
        raise ValueError(f"такого метода нет: {method}")
    