from maths.factorial import FactorialCalculator
from maths.fibonacci import FibonacciCalculator
from sorting.bubble import BubbleSort
from sorting.quick import QuickSort
from sorting.counting import CountingSort
from sorting.heap import HeapSort
from sorting.radix import RadixSort
from sorting.bucket import BucketSort
from structures.stack import Stack
from structures.queue import Queue

def main():
    choice = input()
    
    if choice == "факториал":
        n = int(input())
        method = input()
        print(FactorialCalculator.calculate(n, method))
    
    elif choice == "фибоначчи":
        n = int(input())
        method = input()
        if method == "iterative":
            print(FibonacciCalculator.iterative(n))
        else:
            print(FibonacciCalculator.recursive(n))
    
    elif choice == "сортировка":
        algo = input()
        nums = list(map(int, input().split()))
        
        if algo == "bubble":
            print(BubbleSort().sort(nums))
        elif algo == "quick":
            print(QuickSort().sort(nums))
        elif algo == "counting":
            print(CountingSort().sort(nums))
        elif algo == "heap":
            print(HeapSort().sort(nums))
        elif algo == "radix":
            print(RadixSort().sort(nums))
        elif algo == "bucket":
            print(BucketSort().sort([float(x) for x in nums]))
    
    elif choice == "стек":
        s = Stack()
        while True:
            cmd = input()
            if cmd == "end":
                break
            elif cmd == "push":
                s.push(input())
            elif cmd == "pop":
                print(s.pop())
            elif cmd == "peek":
                print(s.peek())
    
    elif choice == "очередь":
        q = Queue()
        while True:
            cmd = input()
            if cmd == "end":
                break
            elif cmd == "enqueue":
                q.enqueue(input())
            elif cmd == "dequeue":
                print(q.dequeue())
            elif cmd == "front":
                print(q.front())

if __name__ == "__main__":
    main()