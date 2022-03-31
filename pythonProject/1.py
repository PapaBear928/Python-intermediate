#Pracujesz w  SZIN (Super Zwariowany Instytut Naukowy).
# W SZIN dużą wagę przykłada się do tego, aby funkcje działały szybko!
# Dlatego powstał pomysł, aby każda strategiczna funkcja posiadała wrapper,
# który zmierzy czas wykonania danej funkcji.

import time

def wrap(a_function):
	def a_wrpapped_function(*args, **kwargs):
		time_start = time.time()
		v = a_function(*args,**kwargs)
		time_stop = time.time()
		print(f"Funkcja {a_wrpapped_function} wykonana w czasie {time_stop-time_start}")
		return v
	return a_wrpapped_function

def get_sequence(n):
	if n <= 0:
		return 1
	else:
		v = 0
		for i in range(n):
			v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
		return v

print(get_sequence(9))

wrapper_get_sequence = wrap(get_sequence)

print(get_sequence(9))

print(wrapper_get_sequence(9))

#ver 2.

import functools

def wrap(a_function):
	def a_wrpapped_function(*args, **kwargs):
		time_start = time.time()
		v = a_function(*args,**kwargs)
		time_stop = time.time()
		print(f"Funkcja {a_wrpapped_function} wykonana w czasie {time_stop-time_start}")
		return v
	return a_wrpapped_function

@wrapper_time
def get_sequence(n):
	if n <= 0:
		return 1
	else:
		v = 0
		for i in range(n):
			v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
		return v