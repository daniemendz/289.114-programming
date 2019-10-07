def setup():
    size(600,600,P3D) #3d render, P2D 2d render
    
r = 0

def draw():
    global r
    background('#004477')
    stroke('#ffffff')
    strokeWeight(3)
    
    rect(0,0,100,100)
