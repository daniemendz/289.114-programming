

def setup():
    size(800,800)
    background('#004477')
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
r = 100


def draw():
    global x,y,t,r
    translate(width/2,height/2)
    stroke('#0099ff')
    line(width/2*-1,0, width/2,0)
    line(0,height/2*-1, 0,width/2)
    
    stroke('#ffffff')
    
    '''
    #parabola
    y = parabola(x)
    point(x,y)
    x += 1

    #circle
    xy = circle_(t)
    x = xy[0] * r
    y = xy[1] * r
    point(x,y)
    t += 0.01
    '''
    
    #lissajous
    xy = lissajous(t,100,100,3,2)
    x = xy[0]
    y = xy[1]
    point(x,y)
    t += 0.01
    
    xy = lissajous(t,300,150,154,693)
    stroke('#FF00000')
    x = xy[0]
    y = xy[1]
    point(x,y)
    t += 0.01
