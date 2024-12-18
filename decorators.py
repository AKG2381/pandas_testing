from time import perf_counter


total_time= {}
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling the decorated function...")
        result = func(*args, **kwargs)
        print("Done calling the decorated function.")
        return result
    return wrapper


@decorator
def say_hello(n):
    time = perf_counter()
    for i in range(n):
         print(i)
    final_time = perf_counter() - time
    return final_time

total_time['fisrt'] = say_hello(100000)
total_time['second'] = say_hello(1000)

print(total_time)

