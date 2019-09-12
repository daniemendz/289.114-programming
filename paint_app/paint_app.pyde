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
clearall = False
brush = 'draw'

#stop start draw
def mousePressed():
    if mouseButton == LEFT:
        loop() #starts running draw func
    
    global brushcolour, brushshape, brushsize, clearall
    
    if mouseX < 30:
        if mouseY < 30:
            brushcolour = rainbow[0]
        elif mouseY < 60:
            brushcolour = rainbow[1]
        elif mouseY < 90:
            brushcolour = rainbow[2]
    elif mouseX < 60:
        if mouseY < 30:
            brushcolour = rainbow[3]
        elif mouseY < 60:
            brushcolour = rainbow[4]
        elif mouseY < 90:
            brushcolour = rainbow[5]
    
    if mouseY> height-30 and mouseX<60:
        clearall = True
        redraw()
    
def mouseReleased():
    noLoop()
    global painting 
    painting = False

def mouseWheel(e): # event, records
    global brushsize, paintmode
    
    paintmode = 'select'
    brushsize += e.count
    if brushsize < 3:
        brushsize = 3
    if brushsize > 45:
        brushsize = 45
    
    redraw()

def draw():
    global painting, paintmode, brushsize
    print(frameCount)
    
    if mouseX < 60:
        paintmode = 'select'
    else:
        paintmode = 'free'
    
    if paintmode == 'free':
        if not painting and frameCount>1:
            line(mouseX, mouseY, pmouseX, pmouseY)
            painting = True
        elif painting:
            stroke(brushcolour)
            strokeCap(brushshape)
            strokeWeight(brushsize)
            line(mouseX,mouseY, pmouseX,pmouseY)       
    
    print(paintmode)
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
    
    # brush preview
    fill(brushcolour)
    if brushshape == ROUND:
        ellipse(30,123, brushsize,brushsize)
    paintmode = 'free'
    
    #clear button
    global clearall
    fill('#FFFFFF')
    text('clear', 10, height-12)
    
    if clearall:
        fill('#004466')
        rect(60,0,width, height)
        clearall = False 
        
    # mouse cursor
    if brushsize < 15:
        cursor(CROSS)
    else:
        mousecursor = loadImage('brush-cursor.png')
        mousecursor.resize(brushsize, brushsize)
        cursor(mousecursor)
