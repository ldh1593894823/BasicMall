import string
import random


def gen_code(count, long):
    r = []
    base_string = string.digits + string.ascii_letters
    for i in range(count):
        card_code = ''
        for j in range(long):
            card_code += random.choice(base_string)
        r.append(card_code)
    return r
