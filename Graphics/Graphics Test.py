# Test area
import turtle

turtle.screensize(7000,7000,'white')

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
turtle.forward(50)
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
turtle.right(30)
turtle.forward(20)
turtle.left(30)
turtle.backward(15)
turtle.right(30)
turtle.forward(20)
turtle.left(30)
turtle.backward(15)
turtle.right(40)
turtle.forward(20)
turtle.left(50)
turtle.backward(15)

# 22
turtle.right(110)
curve(80,1,'right')

# 23 - 26
turtle.right(180+15)
curve(50,0.5,'right')
curve(20,1,'right')
curve(30,0.25,'right')
turtle.right(180+30)
curve(10,1,'left')

# 27 - 28
turtle.left(30)
turtle.forward(20)
turtle.right(60)
turtle.left(60)

# 29
curve(100,0.5,'left')

# 30
turtle.pu()
turtle.right(50)
turtle.backward(60)

# 31
turtle.pd()
turtle.left(70)
curve(50,0.75,'right')

# 32
turtle.left(60)
turtle.forward(10)

# 33
turtle.right(30)
turtle.forward(50)

# 34
curve(100,1,'right')

# 35
curve(80,1,'left')

# 36
curve(150,1,'right')

# 37
turtle.right(15)
turtle.forward(10)

# 38
turtle.right(60)
curve(50,1.5,'left')

# 39
turtle.right(30)
turtle.forward(15)

# 40
turtle.left(30)
turtle.forward(20)

# 41
curve(50,0.5,'left')

# 42-44
turtle.left(180 - 60)
turtle.forward(5)
turtle.left(10)
turtle.forward(20)
turtle.right(20)
turtle.forward(5)

# 45-53
turtle.right(87)
turtle.forward(170)
# turtle.


# turtle.hideturtle()

window:object = turtle. Screen()
window. exitonclick()