class FibonacciCalculator:
    """
    класс для вычисления чисел фибоначчи.
    """

    @staticmethod
    def iterative(number: int) -> int:
        """
        итеративно вычислить факториал.
        """

        if number < 0:
            raise ValueError("отрицательный индекс")
        
        if number == 0:
            return 0
        
        if number == 1:
            return 1
        
        a,b = 0,1
        for i in range(2,number + 1):
            a,b = b, a + b
        return b
    
    @staticmethod
    def recursive(number: int) -> int:
        """
        рекурсивно вычислить факториал.
        """

        if number < 0:
            raise ValueError("отрицательный индекс")
        if number <= 1:
            return number
        return FibonacciCalculator.recursive(number - 1) + FibonacciCalculator.recursive(number - 2)
    
    @classmethod
    def sequence(cls, number: int) -> list[int]:
        return [cls.iterative(n) for  n in range(number)]
    