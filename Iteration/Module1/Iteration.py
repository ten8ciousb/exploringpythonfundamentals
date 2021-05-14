print(f"\n______\nCount\n______")

class Count:
    def __init__(self, limit):
        self.limit = limit
        
    def __getitem__(self, index):
        # if index is less than self.limit, return index
        if index < self.limit:
            return index
        else :
            raise IndexError(f"Index error {index} outside limit {self.limit}")

print(f"\nCount Test\n______")

try:
    counter = Count(5)
    for i in counter:
        print(f"at {i}: {counter[i]}")

    print(f"counter[0]: {counter[0]}")
    print(f"counter[4]: {counter[4]}")
    print(f"counter[5]: {counter[5]}")


except IndexError as err:
    print(f"IndexError: {err}")



print(f"\n______\nFibonacci\n______")
class Fibonacci:
    def __init__(self, limit):
        # set the maximum number of Fibonacci numbers
        self.limit = limit
        self.last = 1
        self.current = 1
        
    def __getitem__(self, index):
        if index in (0,1):
            # print(f"index in (0,1)")
            return 1
        
        if index < self.limit:
            # implement creating and returning a Fibonacci number here
            # you can use more than one if or elif if you want
            # 1, 1, 2, 3, 5, ...
            # for i in range(2, index + 1):
            #     print(f"i {i}: index: {index} current: {self.current} last: {self.last}")
            #     fib = self.last + self.current
            #     self.last = self.current
            #     self.current = fib
            # return fib
            fib = self.last + self.current
            self.last = self.current
            self.current = fib
            return fib
        else:
            raise IndexError(f"Index error {index} outside limit {self.limit}")



print(f"\nFibonacci Test\n______")
try:
    fib = Fibonacci(5)
    for number in fib:
        print(number)

    print(fib[8])   

except IndexError as err:
    print(f"IndexError: {err}")
