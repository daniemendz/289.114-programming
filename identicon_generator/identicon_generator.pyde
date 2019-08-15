size(500,500)
noStroke()

colourPick = 0

for i in range(1):
    
    if colourPick%2 == 0:
        background('#ffffff')
    else:
        background('#000000')
    
    if colourPick > 5:
        colourPick = 0 
        
    colour = ['#ff8282', '#63faea', '#5efec3', '#7f2e1e', '#bfa3ff', '#7589ff']
    fill(colour[colourPick])
    rect(0,0, 500,16)
    
    
    colourPick += 1
        
    
