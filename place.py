from turtle import *
import random

Screen().setup(width=1.0, height=1.0)
speed(0)

fillcolor('#1793d1')
begin_fill()
penup()
sety(-170)
setpos((-640, 512))
setx(640)
setpos((0, -170))
end_fill()

fillcolor('#d70a53')
begin_fill()
sety(-512)
setx(640)
sety(512)
end_fill()

setx(-640)

fillcolor('#072c61')
begin_fill()
sety(-512)
setx(0)
sety(-170)
end_fill()

//anjoma
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
