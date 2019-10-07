size(800,400)
background('#000000')
strokeWeight(2)
what = createFont("bro.ttf", 90)

csv = loadStrings('the-number-of-new-book-titles-published.csv')
count = 0
img = loadImage('yellowseahorse.png')

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
            
leaf(730,60,0,'#FD5F22')
leaf(732,55,PI/6,'#FD8024')
leaf(737,57,PI/3,'#FDA529')

leaf(740,60,PI/2,'#FDBF2E')
leaf(743,62,(2*PI)/3,'#FD5F22')
leaf(745,63,(5*PI)/6,'#FD8024')

leaf(740,70,PI,'#FDA529')
leaf(740,73,(7*PI)/6,'#FDBF2E')
leaf(735,74,(4*PI)/3,'#FD5F22')

leaf(730,70,PI+(PI/2),'#FD8024')
leaf(730,69,(5*PI)/3,'#FDA529')
leaf(726,65,(11*PI)/6,'#FDBF2E')

pushMatrix()
textFont(what)
translate(790,385)
rotate(-PI/2)
fill('#FDBF2E')
text("5",0,0)
popMatrix()

img.resize(0,370)
image(img,0,15)
