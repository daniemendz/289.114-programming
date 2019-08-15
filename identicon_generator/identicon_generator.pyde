size(500,500)
noStroke()

colour = ['#ff8282', '#5efec3', '#63faea', '#7589ff', '#bfa3ff']
bgcolour = ['#ffffff', '#000000']

for i in range(7):
    
    colourPick = int(random(len(colour)))
    bgcolPick = int(random(len(bgcolour)))
     
    if colourPick > 5:
        colourPick = 0 
        
    background(bgcolour[bgcolPick])
    fill(colour[colourPick])
    rect(0,0, 500,16)
    
        
    
