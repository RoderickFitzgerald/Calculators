from ast import arg
import sys

def Power(base, exponent):
    if (exponent == 0):
        return 1
    else:
        return base * Power(base, exponent -1)
    
print(Power(int(sys.argv[1]), int(sys.argv[2])))