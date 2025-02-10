import re


def try_function(n):
    try:
        digits = float((re.findall(r'\d*\.?\d+', n)[0]))
        return digits
    except:
        return None

def extract_digits(lst):
    lst_return = [try_function(n=n) for n in lst]
    return lst_return

