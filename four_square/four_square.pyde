size(600,600)
noFill()
noStroke()

fill("#FF0000")
rect(width/2,0, width/2, height/2)

fill("004477")
rect(0,0, width/2, height/2)

fill("#6633ff")
rect(0,height/2, width/2, height/2)

fill("#FF9900")
rect(width/2,height/2, width/2, height/2)

x= 100
y = 100
txt='?'

if x>=width/2 and y<=height/2:
    txt = 'R'
elif x>=width/2 and y>height/2:
    txt = 'O'
elif x<width/2 and y>height/2:
    txt ='V'
else:
    txt = 'B'
    

fill("#FFFFFF")
textSize(40)
textAlign(CENTER,CENTER)
text(txt, x,y)
