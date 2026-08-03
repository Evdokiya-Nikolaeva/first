#SquareSpirall.py - Рисование квадратной спирали
import turtle
turtle.bgcolor("gray")
t=turtle.Pen()
sides=6
colors=["blue", "yellow","salmon","green","green","red"]
for x in range (360):
    t.pencolor (colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)