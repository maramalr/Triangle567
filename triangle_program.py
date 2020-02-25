# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple python program to classify triangles
@author: jrr
@author: rk
"""

def classify_triangle(xxx, yyy, zzz):
    """
    your correct code goes here...  Fixxx the faulty logic below until the code passes all of
    you test cases.
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exxxactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      BEWARE: there may be a bug or two in this code
    """
    if not(isinstance(xxx, int) and isinstance(yyy, int) and isinstance(zzz, int)):
        return 'InvalidInput'

    elif xxx <= 0 or yyy <= 0 or zzz <= 0:
        return 'InvalidInput'

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    elif xxx > 200 or yyy > 200 or zzz > 200:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    elif (xxx > (yyy + zzz)) or (yyy > (xxx + zzz)) or (zzz > (xxx + yyy)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    elif xxx == yyy and yyy == zzz and xxx == zzz:
        return 'Equilateral'

    elif (((xxx * xxx) + (yyy * yyy)) == (zzz * zzz)) or ((xxx * xxx) == (yyy * yyy) + (zzz * zzz)):
        return 'Right'

    elif (xxx != yyy) and (yyy != zzz) and (xxx != zzz):
        return 'Scalene'

    else:
        return 'Isoceles'
