import os
import time

def isdigit(s, allowFloat=True, allowNegative=False):
    digits = '0123456789'
    if allowFloat:
        digits += '.'
    if allowNegative:
        if s[0] == '-':
            s = s[1:]
    for c in s:
        if c not in digits:
            return False
    return True

def countdown_display(secs):
    while secs >= 0:
        os.system('clear')
        m, s = divmod(secs, 60)
        if secs <= 5:
            print('\033[1;31m', end='')
        elif secs <= 10:
            print('\033[0;33m', end='')
        else:
            print('\033[0m', end='')
        print(f'{str(int(m)).zfill(2)}:{str(round(s, 1)).zfill(4)}')
        secs -= 0.1
        time.sleep(0.1)
    print('\033[0m', end='')
    return True

def countdown(t):
    t = str(t).replace(' ', '').replace('m', ':')
    if t[-1] == 's':
        t = t[:-1]
    if isdigit(t):
        return countdown_display(float(t))
    elif t.count(':') == 1:
        m, s = t.split(':')
        if isdigit(m, False) and isdigit(s):
            secs = int(m)*60 + float(s)

def demo():
    return countdown(15)
            return countdown_display(secs)
    else:
        return False
        
