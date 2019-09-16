size(200,200)
background('#004477')
fill('#0099ff')
strokeCap(PROJECT)

def face(x,y, gap):
    
    #right half
    noStroke()
    rect(x,0, width,y)
    rect(x+gap, 0, width,height)
    
    #mouth
    mouthy = height-(height-y)/2
    stroke('#000000')
    strokeWeight(6)
    line(x,mouthy, x+gap*2,mouthy)
    
    #eyes
    line(x-gap/2,y/2, x-gap/2, y/2-10 )
    line(x+gap/2,y/2, x+gap/2, y/2-10 )
    
face(80,90, 30)
