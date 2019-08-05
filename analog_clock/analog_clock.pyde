

def setup():
    size(600,600)
    noFill()
    stroke('#ffffff')
    
def draw():
    background('#004477')
    translate(width/2, height/2)
    strokeWeight(3)
    ellipse(0,0, 350,350)
    
    rotate(-PI/2)
    
    #hour hand
    strokeWeight(10)
    print(hour() )
    h = TAU/12*hour()
    rotate(h)
    line(0,0, 100,0)
    
    
    

    
