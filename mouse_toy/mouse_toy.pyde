def setup():
    size(600,600)
    background('#004477')
    frameRate(20)

rainbow = ['#ff0000', '#ff9900', '#ffff00', '#00ff00', '#0099ff', '#6633ff']    

sw = 7

def draw():
    stroke(rainbow[frameCount % len(rainbow)])
    strokeWeight(sw)
    
    if mousePressed and mouseButton == LEFT:
        line(mouseX,mouseY, pmouseX,pmouseY)
