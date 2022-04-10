from functools import wraps

def val_checker(dec_check_func):
    def _val_checker(func_cacl_cube):
        @wraps(func_cacl_cube)
        def wrapper(x):
            if dec_check_func(x):
                return func_cacl_cube(x)
            else:
                raise ValueError(f'wrong val {x}')

        return wrapper
    return _val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

a = calc_cube(5)
print(a)
print(calc_cube.__name__)
a = calc_cube(0)