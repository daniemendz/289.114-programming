size(500,500)
background('#222222')
noStroke()

colourPick = 0

for i in range(2):
    
    if colourPick > 5:
        colourPick = 0 
        
    colour = ['#ff0000', '#ff9900', '#ffff00', '#00ff00', '#0099ff', '#6633ff']
    fill(colour[colourPick])
    rect(0,0, 500,16)
    colourPick += 1
    
    if colourPick%2 == 0:
        fill('#ffffff')
    else:
        fill('#000000')
