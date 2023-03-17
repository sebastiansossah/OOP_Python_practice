import turtle
from random import randint


class Point:

    # To declare the minimum values use a function
    def __init__(self, x, y):
        # X and Y are attributes or instance variables
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False

    def distance(self, other_x, other_y):
        return (((other_x - self.x) ** 2) + ((other_y - self.y) ** 2)) ** 0.5


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area_rectangle(self):
        return (self.point1.x - self.point2.x) * (self.point1.y - self.point2.y)


# Inheritanace from rectangle
# Will going all the methods of Rectangle plus all the methods that we create
class GraphicalRectangle(Rectangle):

    def drow(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)

        
# Inheritance from Point class
class GuiPoint(Point):

    def drow(self, canvas, size= 5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)

Rectangle = GraphicalRectangle(Point(randint(0, 400), randint(0, 400)),
                                  Point(randint(10, 400), randint(10, 400)))

print("Rectangle coordinates: ",
        Rectangle.point1.x, ",",
        Rectangle.point1.y, "and",
        Rectangle.point2.x, ",",
        Rectangle.point2.y)

user_point = GuiPoint(float(input("Guess X: ")),
            float(input("Guess Y: ")))

user_area = float(input("Guess rectangle area: "))

print("Your point was inside rectangle: ",
    user_point.falls_in_rectangle(Rectangle))

print("Your area was off by: :",
        Rectangle.area_rectangle()- user_area)

myturtle = turtle.Turtle()
Rectangle.drow(canvas=myturtle)
user_point.drow(canvas=myturtle)
turtle.done()