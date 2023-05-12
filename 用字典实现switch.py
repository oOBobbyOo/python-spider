# 用字典实现switch

day = 0

switcher = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
}

day_name = switcher.get(day, 'Unkown')
print(day_name)


def get_sunday():
    return 'Sunday'


def get_monday():
    return 'Monday'


def get_default():
    return 'Unkown'


switcher_fun = {
    0: get_sunday,
    1: get_monday,
}

day_name2 = switcher_fun.get(day, get_default)()
print(day_name2)
