import math
import sys

def orth2pol(x, y, z):
    r = math.sqrt(x ** 2 + y ** 2 + z ** 2)    
    ## Calculate r from x, y, z ##
    phi = math.atan2(y,x)
    ## Calculate phi using an inverse trigonometric function ##
    theta = math.acos(z / math.sqrt(x ** 2 + y ** 2 + z ** 2))
    ## Calculate theta using an inverse trigonometric function ##
    
    pol = [r, phi, theta]
    return pol

def main():
    print(orth2pol(1, 1, math.sqrt(2)))
    print(orth2pol(1, -1, -math.sqrt(2)))
    print(orth2pol(-math.sqrt(3), 3, -2))

if __name__ == "__main__":
    main()