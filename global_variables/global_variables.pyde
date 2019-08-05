y=1 #global. counting system

def setup():
    size(500,500)
    noFill()
    stroke('#ffffff')
    strokeWeight(3)

def draw():
    global y #makes the global writable
    background('#004477')
    y += 1
    ellipse(height/2,y, 47,47)
    
    if frameCount%100 ==0:
        saveFrame()
