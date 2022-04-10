def type_logger(func):
    def wrapeer(*args):
        print(f'{func.__name__}(', end='')
        for arg in args:
            print(f'{arg}: {type(arg)}', end=', ')

        print(')', end=' return ')
        return func(*args)
    return wrapeer

@type_logger
def cal_cube(*args):
    return list(map(lambda x: x ** 3, args))

print(cal_cube(5))
print(cal_cube(2, 4))