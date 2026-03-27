
# fibonacci series
# 0, 1, 1, 2, 3, 5, 8, 13, 21 .. and so on

def fib(num):
    if num < 2:
        return num
    return fib(num-1)+fib(num-2)

# implementation

print(fib(5))
print(fib(7))

