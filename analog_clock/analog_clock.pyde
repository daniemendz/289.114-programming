

def setup():
    size(600,600)
    noFill()
    stroke('#ffffff')
    
def draw():
    background('#004477')
    translate(width/2, height/2)
    strokeWeight(3)
    ellipse(0,0, 350,350)
    
    rotate(-PI/2) #transforms before matrix are essentially globals
    
    #hour hand
    pushMatrix() #transforms inside matrix are only applicable in it 
    strokeWeight(10)
    print(hour() )
    h = TAU/12*hour()
    rotate(h)
    line(0,0, 100,0)
    popMatrix()
    
    #minute hand
    pushMatrix()
    strokeWeight(5)
    m= TAU/60*minute()
    rotate(m)
    line(0,0, 130,0)
    popMatrix()
    
    #second hand
    pushMatrix()
    strokeWeight(2)
    s= TAU/60*second()
    rotate(s)
    line(0,0, 150,0)
    popMatrix()
    
    
