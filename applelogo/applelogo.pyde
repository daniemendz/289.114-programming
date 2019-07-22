size(800,800)
background('#004477')
#image(loadImage('grid.png'), 0,0)
image(loadImage('apple.png'), 0,0)
noStroke()


#blu
beginShape()
fill('#009edf')
vertex(0,0)
vertex(800,0)
vertex(800,800)
vertex(0,800)
endShape(CLOSE)
#vio
beginShape()
fill('#ad3b9b')
vertex(0,0)
vertex(800,0)
vertex(800,690)
vertex(0,690)
endShape(CLOSE)
#re
beginShape()
fill('#ff373c')
vertex(0,0)
vertex(800,0)
vertex(800,590)
vertex(0,590)
endShape(CLOSE)
#ora
beginShape()
fill('#ff8301')
vertex(0,0)
vertex(800,0)
vertex(800,490)
vertex(0,490)
endShape(CLOSE)
#yelle
beginShape()
fill('#ffb900')
vertex(0,0)
vertex(800,0)
vertex(800,390)
vertex(0,390)
endShape(CLOSE)
#green
beginShape()
fill('#00bc38')
vertex(0,0)
vertex(800,0)
vertex(800,290)
vertex(0,290)
endShape(CLOSE) 

#white
beginShape()
fill('#ffffff')
noStroke()
noFill()
vertex(0,0)
bezierVertex(800,0, 800,0, 800,0)
bezierVertex(800,800,800,800, 800,800)
bezierVertex(0,800, 0,800, 0,800)
bezierVertex(0,0,0,0, 0,0)
beginContour()
stroke(1)
vertex(400,750)
bezierVertex(320,750, 280,820, 190,740)
bezierVertex(110,680, 60,560, 55,490)
bezierVertex(40,260, 160,195, 260,195)
endContour()
endShape() 
