__author__ = 'Admin'
fibonacci = lambda x: fibonacci(x-2) + fibonacci(x-1) if x > 2 else 1
print(fibonacci(10))
