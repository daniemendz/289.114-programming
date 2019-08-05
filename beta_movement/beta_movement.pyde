def setup():
    frameRate(12) #beta movement less than 12 fps
    size(500,500)
    background('#004477')
    noFill()
    stroke('#ffffff')
    strokeWeight(3)

def draw():
    background('#004477')
    if frameCount%2 == 0: 
        ellipse(250,140, 47,47)
    else:
        ellipse(250,height-140, 47,47)
    
