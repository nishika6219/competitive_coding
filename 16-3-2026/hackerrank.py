
import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hr   = int(s[0:2])
    min  = int(s[3:5])
    sec  = int(s[6:8])
    ampm = s[8:10]
    
    if ampm == "PM" and hr != 12:
        hr += 12
    if ampm == "AM" and hr == 12:
        hr = 0
    return f"{hr:02d}:{min:02d}:{sec:02d}"


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()