#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
  sides = sorted([a,b,c])
  
  for side in sides:
    if side < 1: raise TriangleError
  if sides[0] + sides[1] < sides[2]: raise TriangleError
  
  
  set_of_sides = set(sides)
  if len(set_of_sides) == 1:
    return 'equilateral'
  elif len(set_of_sides) == 2:
    return 'isosceles'
  return 'scalene'


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
