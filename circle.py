#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: September 2019
# This is a program which can find the area of a circle.


import constants

radius = int(input("Input the radius of the circle:"))
circumference = constants.TAU*radius


def main():
    print("If a circle has the radius {}cm" .format(radius))
    print("")
    print("Then the area of the circle is {}cm^2" .format(circumference))


if __name__ == "__main__":
    main()
