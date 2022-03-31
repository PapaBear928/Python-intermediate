import functools
import time

@functools.lru_cache()
def fib(n):
	time.sleep(0.15)
	if n <= 2:
		result = n
	else:
		result = fib(n - 1) + fib(n - 2)
	return result
start = time.time()
for i in range(1,41):
	print('()! = ()' .format(i, fib(i)))
	stop = time.time()
	print(stop-start)
print(fib(40))