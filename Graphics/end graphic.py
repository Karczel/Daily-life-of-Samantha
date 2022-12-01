import turtle

def curve(length,degree,direction):
    for i in range(length):
        turtle.forward(1)
        if direction == 'left':
            turtle.left(degree)
        if direction == 'right':
            turtle.right(degree)

# - "The end" text -
turtle.pu()
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(153)
turtle.write("- The end -",font=("Courier",45,"bold"))
turtle.backward(153)
turtle.right(90)
turtle.backward(100)

# - z z z -
# 1
turtle.left(90)
turtle.forward(133+50)
turtle.write("Z",font=('Courier',32,'normal'))
# 2
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(27)
turtle.write("Z",font=('Courier',20,'normal'))
# 3
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(22)
turtle.write("Z",font=('Courier',16,'normal'))
# 4
turtle.forward(163+100)
turtle.write("Z",font=('Courier',16,'normal'))
# 5
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.write("Z",font=('Courier',20,'normal'))
# 6
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.write("Z",font=('Courier',32,'normal'))

turtle.backward(113+50)
turtle.left(90)
turtle.backward(100)

# - Samantha -
turtle.right(180)
turtle.right(90)
turtle.forward(100)
turtle.pd()
curve(70,1,'left')

# - Karczel and Samantha

window:object = turtle. Screen()
window. exitonclick()