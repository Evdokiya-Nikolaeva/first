#SpiralMyName.py-печатает цветную спираль имен пользователей

import turtle #Установка графики turtle
t=turtle.Pen()
turtle.bgcolor('black')
colors = ['red','yellow','blue','green']

#Запрос имени пользователя с помощью всплывающего окна textinput
your_name=turtle.textinput('Введите своё имя','Как тебя зовут')

#Нарисовать на экране спираль имён 100 раз
for x in range (100):
    t.pencolor(colors[x%4])#По очереди выбрать все 4 цвета
    t.penup ( )
    t.forward(x*4)#Просто переместить черепаху по экрану
    t.pendown()#Написать имя пользователя, увеличивая каждый раз шрифт
    t.write(your_name,font=('TimesNewRoman',int((x+4)/4),'bold'))
    t.left(92)#Повернуть налево,как в других спиралях.


