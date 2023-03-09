#!/usr/bin/env python3

import sys
import math

def main():
    for line in sys.stdin:
        numbers = line.strip().split()
        start_r = float(numbers[0])
        inc_r = float(numbers[1])
        end_r = float(numbers[2])

        h1 = 'Radius (m)'
        h4 = '-' * len(h1)
        h2 = 'Area (m^2)'
        h5 = '-' * len(h2)
        h3 = 'Volume (m^3)'
        h6 = '-' * len(h3)

        print(f'{h1:>s} {h2:>15s} {h3:>15s}')
        print(f'{h4:>s} {h5:>15s} {h6:>15s}')
        area = 4 * math.pi * (start_r ** 2)
        while start_r <= end_r:
            print(f'{start_r:>10.1f} {(4 * math.pi * (start_r ** 2)):>15.2f} {((4 / 3) * (math.pi) * (start_r ** 3)):>15.2f}')
            start_r += inc_r
if __name__ == '__main__':
    main()
