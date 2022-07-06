import sys

def main():
    print(fib(int(sys.argv[1])))

def fib(n: int) -> int:
    if n <= 1:
        return n

    # use recursion to add the previous numbers would be results of a fibonnaci
    return fib(n - 1) + fib(n - 2)

main()

