size(800,400)
background('#fdbf2d')
stroke('#fd8024')
strokeWeight(2)

csv = loadStrings('the-number-of-new-book-titles-published.csv')
count = 0

h = 0
colorMode(HSB,360,100,100,100)
stroke(h,100,100,100)


def graph():
    for i in range(2,len(csv)): # draws graph
        entry = csv[i].split(',')
        years = int(entry[2])-1500 #years
        publ = entry[3] #published
        yscale = float(height/0.5)/float(2326)
        xscale = float(width)/float(100)
    
        x = (float(xscale)*float(years)) - 1140
        y = (float(yscale)*float(publ)) - 150
        
        prev = i - 1 
        entry = csv[prev].split(',')
        years = int(entry[2])-1500 #years
        publ = entry[3] #published
        px = (float(xscale)*float(years)) - 1140
        py = (float(yscale)*float(publ)) - 150
        
        point(x,y)
        line(x,y, px,py)
    
graph()

ty = 1
for i in range(25):
    translate(0,ty)
    graph()
    ty += 1
    h += 10
    stroke(h,100,100,100)
    
