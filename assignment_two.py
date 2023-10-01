#Steve
#23.09.29

import turtle
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
slope1 = y1/x1
slope2 = y2/x2
#when one of x coordinate is 0, it gets error because of devision by zero, so solving by case
if x1 == 0:
    #when one of the coordinate is 0, 1/slope is tangent value
    tan = 1/slope2
elif x2 == 0:
    tan = 1/slope1
else:
    tan = (slope2-slope1)/(1+slope1*slope2)
#get angle value using arctangent function
angle = abs(math.atan(tan)*180/math.pi)

#go to 0,0 to write number
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
#print number on turtle screen
turtle.write(str(angle), align="center", font=("Comic sans ms", 10, "normal"))
turtle.exitonclick()