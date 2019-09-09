def setup():
    size(600,600)
    background('#004477')
    wendy = createFont('wendy.ttf', 20)
    textFont(wendy)
    noLoop() #holds frame, stops draw func
    noStroke()
    
rainbow = ['#ff0000', '#ff9900', '#ffff00', '#00ff00', '#0099ff', '#6633ff']
brushcolour = rainbow[0]
brushshape = ROUND
brushsize = 4
painting = False
paintmode = 'free'

#stop start draw
def mousePressed():
    if mouseButton == LEFT:
        loop() #starts running draw func
def mouseReleased():
    noLoop()
    global painting 
    painting = False


def draw():
    global painting, paintmode
    print(frameCount)
    
    if paintmode == 'free':
        if not painting and frameCount>1:
            line(mouseX, mouseY, pmouseX, pmouseY)
            painting = True
        elif painting:
            stroke(brushcolour)
            strokeCap(brushshape)
            strokeWeight(brushsize)
            line(mouseX,mouseY, pmouseX,pmouseY)
            
            
    # black panel
    noStroke()
    fill('#000000')
    rect(0,0, 60,height)

    #colour palette 
    fill(rainbow[0]); rect(0,0, 30,30)
    fill(rainbow[1]); rect(0,30, 30,30)
    fill(rainbow[2]); rect(0,60, 30,30)
    fill(rainbow[3]); rect(30,0, 30,30)
    fill(rainbow[4]); rect(30,30, 30,30)
    fill(rainbow[5]); rect(30,60, 30,30)
