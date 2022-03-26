def my_generator(max):
    my_list = (x for x in range(1, max+1, 2))
    for i in list(my_list):
        yield i


my_numbers = my_generator(18)
print(next(my_numbers))
print(next(my_numbers))
print(next(my_numbers))