size(800,800)
grid = loadImage('grid.png')
image(grid, 0,0)
noFill()
stroke("#ffffff")
strokeWeight(3)

#square
beginShape()
vertex(100,100)
vertex(200,100)
vertex(200,200)
vertex(100,200)
endShape(CLOSE)

#s-bend
beginShape()
vertex(400,200)
bezierVertex(
        300,300, #cp for vertex1
        500,500, #cp for vertex2
        400,600
)
endShape()

#heart
beginShape()
vertex(600,400)
bezierVertex(420,300, 550,150, 600,250)
bezierVertex(650,150, 780,300, 600,400)
endShape()
