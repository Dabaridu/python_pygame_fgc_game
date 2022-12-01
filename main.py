#my pyton file.py
from turtle import *
#color('red', 'yellow')
#begin_fill()
#while True:
#    forward(200)
#    left(170)
#    if abs(pos()) < 1:
#        break
#end_fill()
#done()
msg = "hello World"
print(msg)
#----------------------------define variables
crcl = 20
grid = 140
gridsq = 5
xcounter = 0
ycounter = 0
colourcounter = 0
fieldoffset = 5 
pu()
speed(1000)
offsettozero = (-(grid*(gridsq-1))/2)
xgrid = offsettozero
ygrid = offsettozero -20
#--------------------------centedot
home()
pd()
dot()
pu()
#--------------------------drawCross
home()
pd()
setpos(-(((grid)*gridsq-1)/2),0)
setpos((((grid)*gridsq-1)/2),0)
pu()
setpos(0,-(((grid)*gridsq-1)/2))
pd()
setpos(0,-(((grid)*gridsq-1)/2))
setpos(0,(((grid)*gridsq-1)/2))
pu()
#--------------------------drawb0x

#-------------------------draw playfield
while ycounter<gridsq:
    ycounter += 1
    while xcounter<gridsq:
        setpos(xgrid, ygrid)
        colourcounter += 1
        if ((colourcounter == 1)or(colourcounter == gridsq*gridsq)):
            color("red")
        elif ((colourcounter == gridsq)or(colourcounter == gridsq*gridsq-gridsq+1)):
            color("blue")
        else:
             color("black")
        pd()
        circle(crcl)
        pu()
        xgrid += grid
        xcounter += 1
    xcounter = 0
    xgrid = offsettozero
    setpos(xgrid, ygrid)
    ygrid += grid
home()
#----------------------------playgame
done()
#-----------mogoče sem povzročil problem s ukazon keyboardinterupt ki je sprožil nekaj v python skripti, zaženi z debugerjem pa dela
# very nice