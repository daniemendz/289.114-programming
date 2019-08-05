logo = None #empty variable
x = 0
y = 0
xspeed = 2
yspeed = 2
xd = 1


def setup():
    global logo
    size(700,700)
    logo = loadImage('dvd-logo.png')

def draw():
    global x,y, xspeed, yspeed
    background('#000000')
    
    image(logo, x,y)
    x += xspeed
    y += yspeed
    
    if x+100 > width or x<0: 
        xspeed *= -1
    elif y+45> width or y<0:
        yspeed *= -1

    

    
    
