size(800,400)
background('#000000')
strokeWeight(2)

csv = loadStrings('the-number-of-new-book-titles-published.csv')
count = 0

h = -10
colorMode(HSB,360,100,100,100)
stroke(h,100,100,100)
fill(h,100,100,100)

def graph():
    beginShape()
    vertex(-10, 450)
    for i in range(100,400): # draws graph
        entry = csv[i].split(',')
        years = int(entry[2])-1500 #years
        publ = entry[3] #published
        yscale = float(height/0.3)/float(2326)
        xscale = float(width)/float(100)
    
        x = (float(xscale)*float(years)) - 1140
        y = (float(yscale)*float(publ)) - 245
        
        prev = i - 1 
        entry = csv[prev].split(',')
        years = int(entry[2])-1500 #years
        publ = entry[3] #published
        px = (float(xscale)*float(years)) - 1140
        py = (float(yscale)*float(publ)) - 245
        
        vertex(x,y)
        line(x,y, px,py)
    vertex(850, 450)
    endShape(CLOSE)
graph()

ty = 1
tx = 0
pushMatrix()
for i in range(30):
    translate(tx,ty)
    graph()
    ty += 3
    tx -= 1
    h += 3.7
    stroke(h,100,100,100)
    fill(h,100,100,100)
popMatrix()

fill(0xccffffff)
noStroke()
beginShape()
vertex(0,0)
vertex(800,0)
vertex(800,400)
vertex(0,400)
vertex(0,0)
beginContour()
vertex(10,10)
vertex(10, 390)
vertex(600,390)
vertex(600,10)
vertex(10,10)
endContour()
endShape(CLOSE)
