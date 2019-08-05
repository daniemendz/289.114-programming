theta = 0
radius = 1
s = 200 #scale variable

def setup():
    size(600,600)
    noFill()
    stroke('#ffffff')
    strokeWeight(3)
    
def draw():
    global theta
    background('#004477')
    translate(width/2, height/2)
    diameter = radius*s*2
    strokeWeight(3)
    ellipse(0,0, diameter,diameter)
    
    x = cos(theta)
    y = sin(theta)
    
    line(0,0, x*s, y*s)
    
    ellipse( -height/2+40,y*s, 3,3)
    ellipse(x*s*1, -width/2+40, 3,3)
    
    strokeWeight(1)
    line(-height/2+40,y*s, x*s, y*s)
    line(x*s,-width/2+40, x*s, y*s)
    
    theta += 0.1
    
