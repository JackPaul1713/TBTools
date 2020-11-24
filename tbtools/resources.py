# Name: resources
# Description: Resources

#INIT#
#import#
import os

#func#
def is_numb(str):
    try:
        int(str)
        return(True)
    except ValueError:
        return(False)

def clear():
    print(chr(27) + "[2J")

    #MAIN#
if __name__ == '__main__':
    print('no testing at this point')

# Author: Jack Martin
# Start: 11/23/2020, Completion: