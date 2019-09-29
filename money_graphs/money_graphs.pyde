size(800,400)
background('#fdbf2d')
stroke('#fd8024')
strokeWeight(3)

csv = loadStrings('the-number-of-new-book-titles-published.csv')

for i in range(140,240):
    entry = csv[i].split(',')
    years = int(entry[2])-1500 #years
    publ = entry[3] #published
    yscale = float(height/0.5)/float(2326)
    xscale = float(width)/float(100)
    x = (float(xscale)*float(years)) - 1105
    y = (float(yscale)*float(publ)) + 340
    
    prev = i - 1 
    entry = csv[prev].split(',')
    years = int(entry[2])-1500 #years
    publ = entry[3] #published
    px = (float(xscale)*float(years)) - 1105
    py = (float(yscale)*float(publ)) +340
    
    point(x,y)
    line(x,y, px,py)
