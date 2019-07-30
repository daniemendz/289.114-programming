size(500,500)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

i=0

while i<24:
    ellipse(width/2, height/2, 30*i,30*i)
    i=i+1
