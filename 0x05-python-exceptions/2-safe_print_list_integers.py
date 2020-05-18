def safe_print_list_integers(my_list=[], x=0):
    size = 0
    for i in range(0, x):
            try:
                print("{:d}".format(my_list[i]), end="")
                size += 1
            except (TypeError, ValueError):
                pass
    print()
    return size
