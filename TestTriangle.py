# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle_program import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def test_RightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right')
        self.assertEqual(classify_triangle(5,3,4),'Right')
        
    def test_EquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral')

    def test_IsocelesTriangles(self): 
        self.assertEqual(classify_triangle(3,3,1),'Isoceles')
        self.assertEqual(classify_triangle(2,3,2),'Isoceles')
        self.assertEqual(classify_triangle(3,2,2),'Isoceles')

    def test_ScaleneTriangles(self): 
        self.assertEqual(classify_triangle(1,3,2),'Scalene')

    def test_NotvalidTriangles(self):
        self.assertEqual(classify_triangle(5,9,3), 'NotATriangle')

    def test_InvalidInput(self):
        self.assertEqual(classify_triangle(0,1,2), 'InvalidInput')
        self.assertEqual(classify_triangle(1,0,2), 'InvalidInput')
        self.assertEqual(classify_triangle(2,1,0), 'InvalidInput')
        self.assertEqual(classify_triangle(-3,1,2), 'InvalidInput')
        self.assertEqual(classify_triangle(1,-3,2), 'InvalidInput')
        self.assertEqual(classify_triangle(2,1,-3), 'InvalidInput')
        self.assertEqual(classify_triangle(300,150,200), 'InvalidInput')
        self.assertEqual(classify_triangle(90,201,100), 'InvalidInput')
        self.assertEqual(classify_triangle(59,90,203), 'InvalidInput')
        self.assertEqual(classify_triangle(1,0.1,2), 'InvalidInput')
        self.assertEqual(classify_triangle('A',1,2), 'InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)

