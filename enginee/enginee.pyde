theta = 0
radius = 1
s = 40 #scale variable

def setup():
    size(600,600)
    noFill()
    stroke('#ffffff')
    strokeWeight(3)
    
def draw():
    global theta
    background('#004477')
    
    pushMatrix()
    translate(width/4+width/2+10, height/2)
    diameter = radius*s*2
    strokeWeight(3)
    ellipse(0,0, diameter,diameter)
    
    x = cos(theta)
    y = sin(theta)
    z = -cos(theta)
    
    line(0,0, x*s, y*s)

    #ellipse(x*s*1, -width/2+40, 3,3)
    ellipse(0, y*s*1-100, 3,3)
    line(0,y*s*1-100, x*s, y*s)
    
    
    quad(-25,y*s*1-130, 25,y*s*1-130, 25,y*s*1-90, -25,y*s*1-90)
    line(-25,y*s*1-120, 25,y*s*1-120)
    popMatrix()

    pushMatrix()
    translate(width/4-60, height/2)
    line(0, z*s*1-100, 0, z*s*1-0)
    quad(-25,z*s*1-130, 25,z*s*1-130, 25,z*s*1-90, -25,z*s*1-90)
    line(-25,z*s*1-120, 25,z*s*1-120)
    popMatrix()
    
    pushMatrix()
    translate(width/4+20, height/2)
    line(0, x*s*1-100, 0, x*s*1-0)
    quad(-25,x*s*1-130, 25,x*s*1-130, 25,x*s*1-90, -25,x*s*1-90)
    line(-25,x*s*1-120, 25,x*s*1-120)
    popMatrix()
    
    pushMatrix()
    translate(width/4+100, height/2)
    line(0, y*s*1-100, 0, y*s*1-0)
    quad(-25,y*s*1-130, 25,y*s*1-130, 25,y*s*1-90, -25,y*s*1-90)
    line(-25,y*s*1-120, 25,y*s*1-120)
    popMatrix()

    theta += 0.1
    
