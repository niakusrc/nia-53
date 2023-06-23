import datetime
from preprocessing import preprocessing
import sys
if __name__ == '__main__':
    print('[*] Program Starts')
    print('Time is : ', datetime.datetime.now())
    print('[*] Command : python main.py')
    print('[!] Preprocessing Start')
    print('Time is : ', datetime.datetime.now())
    preprocessing()
    print('[*] Preprocessing End')
    print('Time is : ', datetime.datetime.now())