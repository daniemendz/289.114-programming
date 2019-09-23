def setup():
    size(800,800)
    
location = PVector(300,200)
    
def draw():
    background('#004477')
    
    #amoeba
    global location
    fill(0x880099ff)
    stroke('#ffffff')
    strokeWeight(3)
    location += PVector(0.3,0.3)
    ellipse(location.x,location.y, 200,200)
