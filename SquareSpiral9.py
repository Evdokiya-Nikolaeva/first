#SquareSpirall.py - Рисование квадратной спирали
import turtle
turtle.bgcolor("black")
t=turtle.Pen()
colors=["blue", "yellow","salmon","green"]
for x in range (100):
    t.pencolor (colors[x%4])
    t.circle(x)
    t.left(91)
    
