size(600,600)
noStroke()

colour = ['#ff9494', '#5efec3', '#63faea', '#7589ff', '#bfa3ff']
bgcolour = ['#ffffff', '#000000']

col = 0
row = 0
colourPick = int(random(len(colour)))

for i in range(36):
    
    bgcolPick = int(random(len(bgcolour)))
    
    if colourPick > 5:
        colourPick = 0 
    
    fill(bgcolour[bgcolPick])
    rect(row*100,col*100, 100,100)
    
    fill(colour[colourPick])
    
    rec = int(random(4))
    
    if colourPick == 1 and rec == 1:
        rect(row*100,col*100, 20,100)
    elif rec == 2:
        rect(row*100,col*100, 100,20)

    
    row += 1
    
    if row%6==0:
        row = 0
        col += 1
    
    
    
    
    
    
