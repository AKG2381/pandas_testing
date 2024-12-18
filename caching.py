
import time
from functools import lru_cache

# Fibonacci without cache
def fibonacci_no_cache(n):
    if n < 2:
        return n
    return fibonacci_no_cache(n-1) + fibonacci_no_cache(n-2)

# Fibonacci with lru_cache (as a substitute for cache)
@lru_cache(maxsize=None)  # Equivalent to cache in function
def fibonacci_with_cache(n):
    if n < 2:
        return n
    return fibonacci_with_cache(n-1) + fibonacci_with_cache(n-2)

# Timing the Fibonacci function without cache
start_no_cache = time.time()
fibonacci_no_cache(30)  # Using a smaller number to avoid long computation times
end_no_cache = time.time()
time_no_cache = end_no_cache - start_no_cache

# Timing the Fibonacci function with cache
start_with_cache = time.time()
fibonacci_with_cache(30)
end_with_cache = time.time()
time_with_cache = end_with_cache - start_with_cache

print(time_no_cache, time_with_cache)