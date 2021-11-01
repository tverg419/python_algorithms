## naive recursive solution
def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

## efficient solution
def fibonacci(num):

    if num <= 1:
        return num

    else:
        fib = [None] * (num + 1)
        fib[0] = 0
        fib[1] = 1
        for i in range(2, num + 1):
            fib[i] = fib[i-1] + fib[i-2]
            
        return fib[num]
print(fibonacci(3))