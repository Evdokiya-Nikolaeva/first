#SquareSpirall.py - Рисование квадратной спирали
import turtle
t=turtle.Pen()
colors=["blue", "yellow","salmon","green")
for x in range (100):
    t.pencolor (colors[x%4])
    t.forward(x)
    t.left(91)
    
