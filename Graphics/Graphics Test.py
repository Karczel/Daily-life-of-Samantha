# Test area
import turtle

turtle.screensize(10000,10000,'white')

def curve(length,degree,direction):
    for i in range(length):
        turtle.forward(1)
        if direction == 'left':
            turtle.left(degree)
        if direction == 'right':
            turtle.right(degree)

turtle.pu()
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
# -- start --
# 1
turtle.pd()
turtle.right(54)
curve(60,1,'left')

# 2
turtle.left(6)
curve(86,0.25,'left')

# 3
turtle.right(15)
curve(180,0.25,'left')

# 4
turtle.right(180)
turtle.right(10)
curve(160,0.2,'right')

# 5
turtle.right(180)
turtle.left(20)
curve(150,0.2,'left')

# 6
turtle.right(180)
turtle.right(10)
curve(100,0.15,'right')

# 7***
turtle.right(180)
turtle.left(20)
turtle.forward(50)

# 8
turtle.left(10)
curve(80,0.3,'left')

# 9
turtle.right(180)
turtle.right(15)
curve(160,0.25,'right')

# 10
curve(100,1,'right')


# 11 - 20
turtle.left(60)
turtle.forward(20)
turtle.left(20)
turtle.backward(15)
turtle.right(30)
turtle.forward(20)
turtle.left(30)
turtle.backward(15)
turtle.right(31)
turtle.forward(23)
turtle.left(30)
turtle.backward(15)
turtle.right(32)
turtle.forward(23)
turtle.left(30)
turtle.backward(16)
turtle.right(43)
turtle.forward(23)
turtle.left(50)
turtle.backward(17)

# 22
turtle.right(110)
curve(60,1,'right')

# 23 - 26
turtle.right(180+2)
curve(20,1.5,'right')
curve(20,3,'right')
turtle.right(30)
curve(30,0.25,'right')
turtle.right(180+50)
curve(30,1,'left')

# 27 - 28
turtle.left(30)
turtle.forward(50)
turtle.right(38)
turtle.forward(77)
turtle.left(60)

# 29
curve(100,0.5,'left')

# 30
turtle.pu()
turtle.right(23)
turtle.backward(92)

# 31
turtle.pd()
turtle.right(70)
curve(100,0.75,'right')

# 32
turtle.left(30)
turtle.forward(10)

# 33
turtle.right(30)
turtle.forward(30)

# 34
curve(100,0.75,'right')

# 35
curve(50,1.2,'left')

# 36
curve(90,1,'right')

# 37
turtle.right(30)
turtle.forward(30)

# 38
turtle.right(75)
curve(80,1.5,'left')

# 39
turtle.right(45)
turtle.forward(46)

# 40
turtle.left(30)
turtle.forward(50)

# 41
curve(80,0.75,'left')

# 42-44
turtle.left(180 - 80)
turtle.forward(10)
turtle.left(10)
turtle.forward(40)
turtle.right(20)
turtle.forward(10)

# 45-53
turtle.right(85)
turtle.forward(160)
turtle.left(90+12)
turtle.forward(50)
turtle.right(15)
turtle.forward(100)
turtle.left(50)
turtle.forward(25)
turtle.left(45)
turtle.forward(80)
turtle.right(20)
turtle.forward(30)
turtle.left(40)
turtle.forward(30)
turtle.right(10)
turtle.forward(20)
turtle.right(5)
turtle.forward(30)

turtle.pu()


# turtle.pencolor(r,g,b)
# turtle.fillcolor(r,g,b)
# turtle.hideturtle()

window:object = turtle. Screen()
window. exitonclick()