def setup():
    size(800,800)

class Amoeba:
    def __init__(self, x,y, xspeed,yspeed, diameter):
        self.location = PVector(x,y)
        self.velocity = PVector(xspeed, yspeed)
        self.diameter = float(diameter)
        
    def update(self):
        fill(0x880099ff)
        stroke('#ffffff')
        strokeWeight(3)
        self.location += self.velocity 
        ellipse(self.location.x,self.location.y, self.diameter,self.diameter)

a = Amoeba(300,200, 0.3,0.3, 150)
b = Amoeba(100,100, 0.4, -0.1, 60)

def draw():
    background('#004477')
    
    a.update()
    b.update()
