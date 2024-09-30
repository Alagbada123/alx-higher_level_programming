#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	"""Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
	A = 0
	for i in range(x):
		try:
			print("{}".format(my_list[]), end="")
			A += 1
		except IndexError:
			break
	print("")
	return (A)
