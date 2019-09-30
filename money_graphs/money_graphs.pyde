size(800,400)
background('#000000')
strokeWeight(2)

csv = loadStrings('the-number-of-new-book-titles-published.csv')
count = 0

h = 3
fill('#000000')
colorMode(HSB,360,100,100,100)
stroke(h,100,100,100)

def graph():
    
    beginShape()
    vertex(-10, 450)
    for i in range(150,400): # draws graph
        entry = csv[i].split(',')
        years = int(entry[2])-1500 #years
        publ = entry[3] #published
        yscale = float(height/0.5)/float(2326)
        xscale = float(width)/float(100)
    
        x = (float(xscale)*float(years)) - 1140
        y = (float(yscale)*float(publ)) - 145
        
        prev = i - 1 
        entry = csv[prev].split(',')
        years = int(entry[2])-1500 #years
        publ = entry[3] #published
        px = (float(xscale)*float(years)) - 1140
        py = (float(yscale)*float(publ)) - 145
        
        vertex(x,y)
        line(x,y, px,py)
    vertex(850, 450)
    endShape(CLOSE)
graph()

ty = 1
tx = 0
for i in range(45):
    translate(tx,ty)
    graph()
    ty += 0.5
    tx-= 0.5
    h += 1.3
    stroke(h,100,100,100)
