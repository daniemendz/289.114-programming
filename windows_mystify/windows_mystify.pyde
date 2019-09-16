
def setup():
    size(800,800)
    background('#000000')
    strokeWeight(3)

def parabola(x):
    return x*x

def circle_(t):
    x = cos(t)
    y = sin(t)
    return [x,y] #returning multiple values using array

def lissajous(t, a,b, kx,ky):
    x = a * cos(kx*t)
    y = b * sin(ky*t)
    return [x,y]
        

#globals
x = -300.0
y = 0.0
t = 0.0
h=1    


def draw():
    global x,y,t,r,h
    
    colorMode(HSB,360,100,100,100)
    fill(0,0,0,15)
    rect(-10,-10,width+20,height+20)
    
    translate(width/2,height/2)

    stroke('#ffffff')
    
    xy1 = lissajous(t, 2,1,3,1)
    x1 = xy1[0] *100
    y1 = xy1[1] *100
    point(x1, y1)
    t += 0.005
    xy2 = lissajous(t, 1,5,5,3)
    x2 = xy2[0] *100
    y2 = xy2[1] *100
    point(x2, y2)
    t += 0.001
    xy3 = lissajous(t, 7,2,5,4)
    x3 = xy3[0] *100
    y3 = xy3[1] *100
    point(x3, y3)
    t += 0.001
    
    stroke(h,100,100,100)
    line(x1,y1,x2,y2)
    line(x1,y1,x3,y3)
    line(x3,y3,x2,y2)
    h += 1
    
    
    xy1 = lissajous(t, 2,1,3,1)
    x1 = xy1[0] *100
    y1 = xy1[1] *100
    point(x1, y1)
    t += 0.005
    xy2 = lissajous(t, 1,5,5,3)
    x2 = xy2[0] *100
    y2 = xy2[1] *100
    point(x2, y2)
    t += 0.001
    xy3 = lissajous(t, 7,2,5,4)
    x3 = xy3[0] *100
    y3 = xy3[1] *100
    point(x3, y3)
    t += 0.001
    
    stroke(h+70,100,100,100)
    line(x1,y1,x2,y2)
    line(x1,y1,x3,y3)
    line(x3,y3,x2,y2)
    h += 1

    if h > 360:
        h = 0
