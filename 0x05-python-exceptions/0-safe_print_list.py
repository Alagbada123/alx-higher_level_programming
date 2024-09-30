#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	a = 0
	for i in my_list:
		a += 1
	try:
		for j in range(0, x):
			print(my_list[j], end="")
		print()
	except IndexError:
		if x > a:
			print()
			return a
		return x
