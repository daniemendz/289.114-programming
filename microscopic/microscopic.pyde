from amoeba import Amoeba

def setup():
    size(800,800)

amoebaa = []

for i in range(12):
    amoebaa.append(Amoeba(
        random(0,900), #x
        random(0,900), #y
        random(-0.5, 0.5), #xspeed
        random(-0.5, 0.5), #yspeed
        random(50,200) #diameter
    ))


def draw():
    background('#004477')

    for amoeba in amoebaa:
        #mouse attractor
        mouse = PVector(mouseX, mouseY-amoeba.diameter/2)
        goto = PVector.sub(mouse, amoeba.location) #difference between vectors
        goto.div(10000)
        
        if mousePressed:
            goto.mult(-1)
            
        amoeba.velocity.add(goto)
        amoeba.velocity.limit(0.8)
        
        amoeba.update()
    
    
