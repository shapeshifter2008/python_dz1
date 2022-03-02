for i in range(1, 101):
    if (i >= 10 and i < 100):
        num = i % 10
    elif (i >= 100):
        num = i % 100
    else:
        num = i

    if (num == 1):
        print('%d процент' % (i))
    elif (num >= 2 and num <= 4):
        print('%d процентa' % (i))
    else:
        print('%d процентов' % (i))