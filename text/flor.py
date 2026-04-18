from turtle import *
import colorsys
speed(0)
bgcolor("black")
h=0
for j in range(16):
    c=  colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h +=0.005
    rt(90)
    circle(150 - j * 6, 90)
done()
    