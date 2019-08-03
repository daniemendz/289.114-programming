size(600,600)
background('#004477')
fill('#FFFFFF')
noStroke()

#quad(40,40, 40,90, 90,90, 90,40) 
#     x1 y1  x2 y2  x3 y3  x4 y4  Anticlockwise from top left
#squares 45px wide, 20px space, 545 max initial
'''
x1 = 40
y1 = 40

x2 = 40
y2 = 85

x3 = 85
y3 = 85

x4 = 85
y4 = 40
'''

x1 = y1 = x2 = y4 = 40
y2 = x3 = y3 = x4 = 85
count = 0
a = 65

for i in range(1,65):
    rand = random(0,0)
    
    if count==7:
        rand = random(-18,18)
        
    
    quad(x1,y1, x2,y2, x3,y3, x4,y4)
    x1,x2,x3,x4 = x1+rand+a, x2+rand+a, x3+rand+a, x4+rand+a
    y1,y2,y3,y4 = y1+rand, y2+rand, y3+rand, y4+rand
    
    if i%8==0:
        y1,y2,y3,y4 = y1+a, y2+a, y3+a, y4+a
        x1=x2=40
        x3=x4=85
        count +=1
    
    
