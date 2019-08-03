size(600,600)
background('#004477')
fill('#FFFFFF')
noStroke()

x1 = y1 = x2 = y4 = 40
y2 = x3 = y3 = x4 = 85
count = 0
a = 65

for i in range(1,65):

    if count>=7:
        rand1 = -15
        rand2 = 15
    elif count>=6:
        rand1 =-12
        rand2 = 12
    elif count>=5:
        rand1 = -10
        rand2 = 10
    elif count>=4:
        rand1=-8
        rand2=8
    elif count>=3:
        rand1=-6
        rand2=6
    elif count>=2:
        rand1=-4
        rand2=4
    elif count>=1:
        rand1=-2
        rand2=2
    else:
        rand1=rand2=0
    
    quad(x1+random(rand1,rand2),y1+random(rand1,rand2),
         x2+random(rand1,rand2),y2+random(rand1,rand2),
         x3+random(rand1,rand2),y3+random(rand1,rand2),
         x4+random(rand1,rand2),y4+random(rand1,rand2))
    
    x1,x2,x3,x4 = x1+a, x2+a, x3+a, x4+a
    
    if i%8==0:
        y1,y2,y3,y4 = y1+a, y2+a, y3+a, y4+a
        
        x1=x2=40
        x3=x4=85
        
        count +=1
    
    
