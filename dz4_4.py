import units
import sys

args = sys.argv

if len(args) != 2:
    print('Укажите код валюты вторым аргументом')
else:
    print('USD', units.currency_rates(args[1]))