# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
# Kata Author: user578387
# 6 kyu

def recusive_func(value):
    value = sum(value)
    if len(str(value)) >= 2:
        return recusive_func(list(map(int, str(value))))
    return value


def digital_root(n):
    while len(str(n)) > 1:
        n = recusive_func(list(map(int, str(n))))
    return n
    
    

if __name__ == "__main__":
    digital_root(493193)#, 2)
