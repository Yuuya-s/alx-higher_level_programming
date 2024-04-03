#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers of a list.

    Args:
        my_list (list): The list to print integers from.
        x (int): The number of elements of my_list to access.

    Returns:
        The real number of integers printed.
    """
    count = 0  

    try:
        for i in range(x):  
            try:
                print("{:d}".format(my_list[i]), end='')  
                count += 1  
            except (TypeError, ValueError):  
                pass  
    except IndexError:  
        pass  

    print()  
    return count  
