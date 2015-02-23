def fibonacci(x):
    if x <= 2:
        return x
    else:
        return fibonacci(x-1) + fibonacci(x-2)
if __name__ == "__main__":
    print fibonacci(10)
