def setup():
    size(800,800)
    
    
    
x = 300
y = 200
    
    
def draw():
    background('#004477')
    
    #amoeba
    global x, y
    fill(0x880099ff)
    stroke('#ffffff')
    strokeWeight(3)
    
    x += 0.3
    y += 0.3
    
    ellipse(x,y, 200,200)
