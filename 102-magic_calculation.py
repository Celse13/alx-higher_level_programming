#!/usr/bin/python3
def magic_calculation(a, b):
    retun_value = 0
    for n in range(1, 3):
        try:
            if n > a:
                raise Exception('Too far')
            retun_value += a ** b / n
        except Exception:
            retun_value = b + a
            break
    return (retun_value)
