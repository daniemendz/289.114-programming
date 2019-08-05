size(800,800)
noFill()
stroke('#ffffff')
strokeWeight(3)
grid = loadImage('grid.png')
image(grid, 0,0)
grido = loadImage('grid-overlay.png')
rect(400,200, 200,200)

translate(100,-80)
rotate(0.785) 
scale(2,2) #scale of x&y 
#shearX(0.4) #transform edge. shearY

image(grido, 0,0)
stroke('#ffff00')
rect(400,200, 200,200)
