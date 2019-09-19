#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: September 2019
# This is a program which can find the area and perimeter or a circle.


# This is what finds the area and perimeter of the circle.
# Replace the two numbers at the end of lines 12, 14 and 15 with radius
# to continue.
import math

import constants

radius = 8
circumference = constants.TAU*radius


def main():
    print("If a circle has the radius:")
    print("{}cm" .format(radius))
    print("")
    print("Then the area of the circle is {}cm^2" .format(circumference))


if __name__ == "__main__":
    main()
