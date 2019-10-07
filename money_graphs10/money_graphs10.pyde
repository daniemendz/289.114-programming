size(800,400)
background('#000000')
strokeWeight(2)

what = createFont("bro.ttf", 90)
csv = loadStrings('temperature-anomaly.csv')

h = 78
colorMode(HSB,360,100,100,100)
fill(h, 100, 100)
noStroke()

def graph():
    beginShape()
    vertex(-10, 450)
    for i in range(2,len(csv)): # draws graph
        entry = csv[i].split(',')
        years = int(entry[2]) - 1973 #years
        publ = entry[3] #published
        yscale = float(height/0.05)/float(25)
        xscale = float(width)/float(43) 
    
        x = (float(xscale)*float(years)) +650
        y = (float(yscale)*float(publ))  -50
        
        prev = i - 1 
        entry = csv[prev].split(',')
        years = int(entry[2]) - 1973 #years
        publ = entry[3] #published 
        
        px = (float(xscale)*float(years)) +650
        py = (float(yscale)*float(publ))  -50
        
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
    fill(h, 60, 100)
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

def leaf(x,y,angle,shade):
    pushMatrix()
    translate(x,y)    
    rotate(angle)
    fill(shade)

    strokeWeight(1)
    beginShape()
    vertex(-50,5)
    vertex(-15,20)
    vertex(-5,5)
    vertex(-15,-10)
    endShape(CLOSE)
    popMatrix()
            
leaf(730,60,0,'#20416c')
leaf(732,55,PI/6,'#407585')
leaf(737,57,PI/3,'#48b78c')
leaf(740,60,PI/2,'#dcf5a2')

leaf(743,62,(2*PI)/3,'#20416c')
leaf(745,63,(5*PI)/6,'#407585')
leaf(740,70,PI,'#48b78c')
leaf(740,73,(7*PI)/6,'#dcf5a2')

leaf(735,74,(4*PI)/3,'#20416c')
leaf(730,70,PI+(PI/2),'#407585')
leaf(730,69,(5*PI)/3,'#48b78c')
leaf(726,65,(11*PI)/6,'#dcf5a2')

textFont(what)
translate(790,385)
rotate(-PI/2)
fill('#407585')
text("10",0,0)
