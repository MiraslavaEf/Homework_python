import string
from random import choice


def rds(length):
    letter = list(string.ascii_letters)
    p = ''
    for _ in range(length):
        p += choice(letter)
    return p

def rez(str):
    up = 0
    lw = 0
    for i in str:
        if i.isupper():
            up += 1
        else:
            lw += 1
    if up > lw:
        return 1
    elif up == lw:
        return 2
    else:
        return 0

def massiv(length, schet):
    return [rds(length) for _ in range(schet)]

def ratio(array):
    bb = 0
    sb = 0
    equal = 0
    for x in array:
        if rez(x) == 1:
            bb += 1
        elif rez(x) == 0:
            sb += 1
        else:
            equal += 1
    ratio_big = (bb / len(array)) * 100
    ratio_small = (sb / len(array)) * 100
    ratio_equal = (equal / len(array)) * 100
    p = 'B строке {round(ratio_small)}% заглавных букв больше {round(ratio_small)}% \
строк где маленьких букв больше {round(ratio_equal)}% строк где их одинаково'
    return p

print(ratio(massiv(5, 9)))
