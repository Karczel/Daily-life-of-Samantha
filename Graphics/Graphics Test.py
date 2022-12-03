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

# --- Outline ---

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
turtle.forward(27)

turtle.pu()
turtle.left(87)
turtle.forward(16)

#54
turtle.pd()
turtle.left(27)
turtle.forward(47)
turtle.right(97)
turtle.forward(52)

# 55
turtle.pu()
turtle.left(60)
turtle.forward(46)

# 56
turtle.pd()
turtle.left(120)
turtle.forward(15)
turtle.right(56)
turtle.forward(70)

# 57
turtle.pu()
turtle.left(120)
turtle.forward(163)

# 58 - 61
turtle.pd()
turtle.right(140)
turtle.forward(25)
turtle.right(40)
turtle.forward(15)
turtle.left(120)
turtle.forward(20)
turtle.left(25)
turtle.forward(32)

# 62
turtle.pu()
turtle.right(58)
turtle.forward(93)

# 63-65
turtle.pd()
turtle.right(44)
turtle.forward(50)
turtle.right(90)
turtle.forward(30)
turtle.right(60)
turtle.forward(12)

turtle.pu()
turtle.left(110)
turtle.forward(49)

# 66-68
turtle.pd()
turtle.left(59)
turtle.forward(40)
turtle.right(60)
turtle.forward(20)
turtle.right(70)
turtle.forward(27)

# 69
turtle.pu()
turtle.right(26)
turtle.forward(230)

# 70
turtle.pd()
turtle.left(40)
curve(40,0.75,'right')

# 71
turtle.left(56)
curve(45-5,0.75,'right')

# 72
turtle.right(10)
curve(25-5,0.5,'right')

turtle.pu()
turtle.right(52)
turtle.forward(12-5)

# 73
turtle.pd()
turtle.right(112)
curve(45-5,0.8,'left')

# 74
turtle.left(51)
curve(20-5,0.8,'left')

# 75
turtle.right(49)
turtle.forward(15-5)

# 76
turtle.left(120)
turtle.forward(18-5)

# 77
turtle.left(59)
turtle.forward(3)

# 78
curve(10,7,'right')

# 79
turtle.forward(5)

# 80
turtle.left(92)
turtle.forward(20-5)

# 81
turtle.left(83)
curve(20-5,3,'left')

# 82
turtle.left(23)
turtle.forward(15-5)

turtle.pu()
turtle.right(54)
turtle.forward(10-5)

# 83
turtle.pd()
turtle.right(112)
curve(25-5,0.15,'right')


# 84
turtle.right(17)
curve(20-5,1.5,'right')

turtle.pu()
turtle.right(60)
turtle.forward(35-10)

# 85
turtle.pd()
turtle.right(74)
curve(25-5,1,'right')

# 86
turtle.left(139)
curve(28-10,1.5,'left')

turtle.pu()
turtle.right(90)
turtle.forward(10)

# 87
turtle.pd()
turtle.right(94)
curve(10-8,3,'right')

turtle.pu()
turtle.right(30)
turtle.forward(76)

# 88
turtle.pd()
turtle.right(70)
curve(30-15,1.5,'right')

# 89
turtle.pu()
turtle.right(170)
turtle.forward(185)

# 90
turtle.pd()
turtle.left(50)
curve(110,0.9,'left')

# 91
turtle.right(25)
curve(70,1,'left')

# 92
turtle.left(12.3)
turtle.forward(150)

# 93
curve(25,2,'left')

# 94
turtle.forward(40)

# 95
turtle.pu()
turtle.right(5)
turtle.forward(54)

# 96
turtle.pd()
turtle.right(30)
curve(20,4,'right')

# 97
turtle.forward(30)

# 98
turtle.left(5)
curve(20,7,'left')

# 99
turtle.right(180-15)
turtle.forward(10)

# 100
turtle.right(10)
curve(25,0.5,'right')

# 101
curve(20,5,'right')

# 102
curve(17,5,'left')

# 103
turtle.left(25)
turtle.forward(10)

# 104
turtle.left(180 - 20)
curve(15,7,'right')

# 105
curve(40,3,'left')

# 106
turtle.right(180-10)
turtle.forward(30)

# 107
curve(50,2,'right')

# 108
turtle.left(45)
curve(25,0.5,'left')

# 109
turtle.right(10)
curve(60,0.5,'right')

# 110
turtle.right(8)
turtle.forward(85)

turtle.pu()
turtle.left(139)
turtle.forward(28)

# 111
turtle.pd()
turtle.left(5)
curve(20,0.5,'right')

# 112
turtle.right(15)
turtle.forward(30)

# 113
turtle.right(30)
curve(28,0.5,'right')

# 114
turtle.right(10)
curve(20,7,'right')

# 115
turtle.pu()
turtle.right(0)
turtle.forward(10)

# 116
turtle.pd()
turtle.right(50)
turtle.forward(15)

# 117
curve(7,7,'left')

# 118
turtle.left(20)
turtle.forward(15)

# 119
turtle.right(5)
turtle.forward(15)

# 120
turtle.left(50)
turtle.forward(25)

# 121
turtle.left(80)
turtle.forward(5)

# 122
turtle.right(10)
turtle.forward(5)

# 123
turtle.left(10)
turtle.forward(5)

# 124
turtle.left(70)
turtle.forward(15)

# 125
turtle.left(120)
turtle.forward(5)

turtle.pu()
turtle.right(120)
turtle.forward(8)

# 126-128
turtle.pd()
turtle.right(110)
curve(15,8,'left')
turtle.left(40)
curve(10,8,'right')
curve(12,8,'left')

turtle.pu()
turtle.left(70)
turtle.forward(5)

# 129
turtle.pd()
turtle.right(10)
curve(10,0.5,'right')

# 130
turtle.left(20)
turtle.forward(13)

# 131
turtle.left(20)
turtle.forward(15)

turtle.pu()
turtle.left(60)
turtle.forward(15)

# 132
turtle.pd()
turtle.left(120)
curve(8,15,'right')

turtle.pu()
turtle.left(90)
turtle.forward(5)

# 133
turtle.pd()
turtle.left(75)
turtle.forward(10)

# 134
turtle.right(5)
curve(10,1,'right')

turtle.pu()
turtle.right(25)
turtle.forward(48)

# 135
turtle.pd()
turtle.right(15)
curve(50,0.8,'right')


# 136
turtle.right(75)
curve(40,2,'left')

# 137
turtle.left(15)
turtle.forward(70)

# 138
turtle.right(100)
turtle.forward(30)

# 139
turtle.left(60)
curve(45,0.8,'left')

# 140
turtle.right(87)
curve(66,1,'right')

turtle.pu()
turtle.left(180+25)
turtle.forward(118)

# 141
turtle.pd()
turtle.right(110)
turtle.forward(20)

# 142
turtle.right(105)
turtle.forward(20)

# 143
turtle.left(30)
turtle.forward(13)

# 144
turtle.right(30)
turtle.forward(25)

# 145
turtle.right(140)
turtle.forward(20)

# 146
turtle.right(42)
curve(40,1,'left')

# 147
turtle.forward(10)

# 148
turtle.right(30)
curve(150,0.2,'left')

# 149
turtle.left(60)
turtle.forward(30)

# 150
turtle.left(60)
turtle.forward(40)

# 151
turtle.right(30)
turtle.forward(70)

# 152 - 154
turtle.right(60)
turtle.forward(30)
turtle.left(45)
turtle.forward(40)
turtle.left(85)
turtle.forward(40)

# 155
turtle.left(15)
turtle.forward(150)

# 156 -158
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(25)
turtle.left(48)
turtle.forward(80)

turtle.pu()
turtle.backward(45)

# 159
turtle.pd()
turtle.left(25)
curve(30,0.5,'left')

turtle.pu()
turtle.left(10)
turtle.forward(120)

# 160
turtle.pd()
turtle.right(90)
turtle.forward(50)

turtle.pu()
turtle.right(5)
turtle.forward(100)

# 161
turtle.pd()
turtle.right(30)
turtle.forward(50)

turtle.pu()
turtle.right(95)
turtle.forward(250)

# 162
turtle.pd()
turtle.left(24)
curve(20,7,'right')

# 163
turtle.right(60)
turtle.forward(10)

# 164
curve(5,18,'left')

# 165
turtle.left(10)
turtle.forward(15)

# 166
turtle.left(20)
curve(10,5,'left')

# 167
turtle.left(30)
turtle.forward(5)

# 168
curve(6,20,'left')

turtle.pu()
turtle.left(60)
turtle.forward(35)

# 169
turtle.pd()
turtle.left(30)
curve(10,2,'left')

turtle.pu()
turtle.left(120)
turtle.forward(75)

# 170
turtle.pd()
turtle.left(60)
curve(10,2,'right')

turtle.pu()
turtle.left(60)
turtle.forward(250)

# 171
turtle.pd()
turtle.left(70)
turtle.forward(20)

turtle.pu()
turtle.forward(20)

# 172
turtle.pd()
turtle.forward(20)

turtle.pu()
turtle.right(150)
turtle.forward(50)

# 173
turtle.right(30)
turtle.forward(10)

# 174
turtle.right(80)
turtle.forward(30)

# 175
curve(7,25,'right')

# 176
turtle.forward(35)

# 177
turtle.right(20)
curve(5,1,'right')

# 178
turtle.right(10)
curve(8,15,'right')

# --- Fill ---



# --- Shadow outline ---



# --- Shadow fill ---



# --- Almost forgotten ponytail ---






# turtle.pencolor(r,g,b)
# turtle.fillcolor(r,g,b)
# turtle.hideturtle()

window:object = turtle. Screen()
window. exitonclick()