size(800,800)
background('#004477')
noStroke()

csv = loadStrings('list_of_best-selling_video_games.csv')

col = 0
colourPick = 0

for i in range(1,len(csv)):
    entry = csv[i].split('\t')
    sales = entry[1]
    title = entry[2]

    fscale = float(800)/float(170000000)
    fwidth = float(fscale)*float(sales)
    #print(fwidth)
    
    if colourPick > 5:
        colourPick = 0 
    
    colour = ['#ff0000', '#ff9900', '#ffff00', '#00ff00', '#0099ff', '#6633ff']
    fill(colour[colourPick])
    rect(0,col*16, fwidth,16)
    
    col +=1
    colourPick +=1
    
