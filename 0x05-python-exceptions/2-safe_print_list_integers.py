#!/usr/bin/python3
    """Print the first x elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
def safe_print_list_integers(my_list=[], x=0):
    count = 0
	try:
    	for i in range(0, x):
			if isinstance(my_list[i], int):
            	print("{:d}".format(my_list[i]), end="")
            	count += 1
        print()
	except IndexError as P
		return P
    return count
