size(500,500)

grid = loadImage('grid.png')
image(grid, 0,0)

noFill()
strokeWeight(3)

#catmull
stroke('#0099FF')
line(100,100, 400,400)

curveTightness(0)

stroke('#FFFF00')
curve(0,250, 100,100, 400,400, 500,250)

stroke('#FF9900')
#control point
curve(0,250, 0,250, 100,100, 400,400)
curve(100,100, 400,400, 500,250, 500,250)



#bezier
stroke('#FF99FF')
#control points
cp1x = 200 
cp1y = 200
cp2x = 300
cp2y = 300

bezier(
    400,100, #vertex 1
    cp1x,cp1y,
    cp2x,cp2y,
    100,400  #vertex 2
)

stroke('#FF0000')
line(400,100, cp1x,cp1y)
line(100,400, cp2x,cp2y)
