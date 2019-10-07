def setup():
    size(600,600,P3D) #3d render, P2D 2d render
    
r = 0

def draw():
    global r
    background('#000000')
    fill('#ffffff')
    strokeWeight(1)
    stroke('#ffffff')
    translate(width/2,height/2)
    
    rotateX(r)
    rotateY(r)
    rotateZ(r)
    translate(0,0,0)
    directionalLight(126, 126, 126, 0, 0, -1)
    ambientLight(102, 102, 102)
    #sphere(200) #radius
    r += 0.01
    
    
    beginShape()
    vertex(-100, -100, -100)
    vertex( 100, -100, -100)
    vertex(   0,    0,  100)
    
    vertex( 100, -100, -100)
    vertex( 100,  100, -100)
    vertex(   0,    0,  100)
    
    vertex( 100,  100, -100)
    vertex(-100,  100, -100)
    vertex(   0,    0,  100)
    
    vertex(-100,  100, -100)
    vertex(-100, -100, -100)
    vertex(   0,    0,  100)
    endShape()

    box(40)
