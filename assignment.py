# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:36:45 2022

@author: qomon
"""

# Write a definition for a class named Circle with attributes center and radius, where center is a Point object and radius is a number.
# Instantiate a Circle object that represents a circle with its center at (150, 100) and radius 75.
# Write a function named point_in_circle that takes a Circle and a Point and returns True if the Point lies in or on the boundary of the circle.
# Write a function named rect_in_circle that takes a Circle and a Rectangle and returns True if the Rectangle lies entirely in or on the boundary of the circle.







from typing import Tuple

class Point:
  def __init__(self, x: float, y: float):
    self.x = x
    self.y = y

class Circle:
  def __init__(self, center: Point, radius: float):
    self.center = center
    self.radius = radius

def point_in_circle(circle: Circle, point: Point) -> bool:
  return (point.x - circle.center.x) ** 2 + (point.y - circle.center.y) ** 2 <= circle.radius ** 2

def rect_in_circle(circle: Circle, rect: Rectangle) -> bool:
  # Find the points of the rectangle's corners
  top_left = Point(rect.x, rect.y)
  top_right = Point(rect.x + rect.width, rect.y)
  bottom_left = Point(rect.x, rect.y + rect.height)
  bottom_right = Point(rect.x + rect.width, rect.y + rect.height)

  # Check if all the corners of the rectangle are inside the circle
  return (point_in_circle(circle, top_left) and
          point_in_circle(circle, top_right) and
          point_in_circle(circle, bottom_left) and
          point_in_circle(circle, bottom_right))

# Instantiate a circle with center (150, 100) and radius 75
my_circle = Circle(Point(150, 100), 75)

# Check if the point (150, 100) lies in the circle
print(point_in_circle(my_circle, Point(150, 100)))  # True
