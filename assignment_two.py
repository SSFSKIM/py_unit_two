#Steve
#23.09.29

import turtle

import sympy as sp

import math
#get input for 2 coordinates
x1 = int(input('type the x coordinate of the first point: '))
x2 = int(input('type the y coordinate of the first point: '))
y1 = int(input('type the x coordinate of the second point: '))
y2 = int(input('type the y coordinate of the second point: '))
#draw lines with turtle
turtle.goto(x1, y1)
turtle.goto(0, 0)
turtle.goto(x2, y2)

#define limit variables
x_1 = sp.symbols('x_1')
x_2 = sp.symbols('x_2')

#get slope using limit so that it works even when input 0
slope1 = sp.limit(y1/x_1, x_1, x1)
slope2 = sp.limit(y2/x_2, x_2, x2)


#get angle value using arctangent function, using limit to calculate even when division by zero happen

angle = abs(sp.limit(math.atan(slope1), x_1, x1) - sp.limit(math.atan(slope2), x_1, x1)*180/math.pi)

#go to 0,0 to write number
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
#print number on turtle screen
turtle.write(str(angle), align="center", font=("Comic sans ms", 10, "normal"))
turtle.exitonclick()