

def setup():
    size(800,800)
    background('#004477')
    strokeWeight(3)

def parabola(x):
    return x*x

#globals
x = -300.0
y = 0.0
t = 0.0    


def draw():
    global x,y,t
    translate(width/2,height/2)
    stroke('#0099ff')
    line(width/2*-1,0, width/2,0)
    line(0,height/2*-1, 0,width/2)
    
    stroke('#ffffff')
    y = parabola(x)
    point(x,y)
    
    x += 1
