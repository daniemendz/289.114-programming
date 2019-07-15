size(600, 740)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

xco = 400
yco = 440

line(width/2,height/3, xco,yco)

ellipse(width/2,height/2, width/11,width/11)

ellipse(width/2,height/2, width/19,width/19)

line(xco,yco, width-xco,yco)

line(width-xco,yco , width/2,height/3)

ellipse(width/2,height/2, width/5,height/12)
