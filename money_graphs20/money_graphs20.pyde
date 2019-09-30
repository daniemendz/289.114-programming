size(800,400)
background('#000000')
strokeWeight(2)

csv = loadStrings('inequality-of-incomes-chartbook.csv')
count = 0

h = 78
colorMode(HSB,360,100,100,100)
stroke(h,100,100,100)
fill(h,100,100,100)

def graph():
    beginShape()
    vertex(-10, 450)
    for i in range(2,len(csv)): # draws graph
        entry = csv[i].split(',')
        years = int(entry[2]) - 1850 #years
        publ = float(entry[3]) #median
        yscale = float(height/0.05)/float(0.5)
        xscale = float(width)/float(168) 
    
        x = (float(xscale)*float(years))
        y = (float(yscale)*float(publ))
        
        prev = i - 1 
        entry = csv[prev].split(',')
        years = int(entry[2]) - 1850 #years
        publ = entry[3] #published 
        
        px = (float(xscale)*float(years))
        py = (float(yscale)*float(publ))
        
        vertex(x,y)
        line(x,y, px,py)
    vertex(850, 450)
    endShape(CLOSE)
graph()

ty = 1
tx = 0
pushMatrix()
for i in range(35):
    translate(tx,ty)
    graph()
    ty += 2.7
    tx -= 1
    h += 8
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
vertex(650,390)
vertex(650,10)
vertex(10,10)
endContour()
endShape(CLOSE)
