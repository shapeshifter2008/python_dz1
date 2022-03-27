src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
some_list = [num for key, num in enumerate(src) if key > 0 and src[key-1] < num]
print(some_list)