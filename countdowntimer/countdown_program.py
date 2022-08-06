import os
import time
import argparse

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
    secs = round(secs, 1)
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

def countdown(t=15):
    t = str(t).replace(' ', '').replace('m', ':')
    if t[-1] == 's':
        t = t[:-1]
    if isdigit(t):
        return countdown_display(float(t))
    elif t.count(':') == 1:
        m, s = t.split(':')
        if not s:
            s = '0'
        if isdigit(m, False) and isdigit(s):
            secs = int(m)*60 + float(s)
            return countdown_display(secs)
        else:
            return False
    else:
        return False

def countdown_terminal():
    parser = argparse.ArgumentParser(prog ='countdown',
                                     description ='countdown')

    parser.add_argument('time', metavar ='time', type=str, nargs=1, help= 'time')

    args = parser.parse_args()
    try:
        if countdown(args.time[0]):
            os.system('clear')
            print('Countdown finished.')
        else:
            os.system('clear')
            print('Countdown failed.')
    except KeyboardInterrupt:
        os.system('clear')
        print('Countdown stopped.')
