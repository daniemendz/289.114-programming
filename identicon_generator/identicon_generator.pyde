size(600,600)
noStroke()

colour = ['#ff9494', '#5efec3', '#63faea', '#7589ff', '#bfa3ff']
bgcolour = ['#ffffff', '#000000']

col = 0
row = 0
colourPick = int(random(len(colour)))

for i in range(64):
    
    bgcolPick = int(random(len(bgcolour)))
    
    if colourPick > 5:
        colourPick = 0 
    
    fill(bgcolour[bgcolPick])
    rect(row*75,col*75, 75,75)
    
    fill(colour[colourPick])
    
    if int(random(2)) == 1:
        rect(row*75,col*75, 20,75)
    else:
        rect(row*75,col*75, 75,20)
    
    row += 1
    
    if row%8==0:
        row = 0
        col += 1
    
    
    
    
    
    
