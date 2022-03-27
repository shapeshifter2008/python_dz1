my_list = []

def my_generator(max):
    global my_list

    if len(my_list) == 0:
        my_list = (x for x in range(1, max + 1, 2))

    return my_list


my_numbers = my_generator(18)
print(next(my_numbers))
print(next(my_numbers))
print(next(my_numbers))