size(500,500)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

i = 0
x = 100
y = 100

while i < 20:
    if x < 450:
        ellipse(x,y, 80,80)
        x += 100
    else:
        y += 100
        x = 100
    i += 1 
    print(i)
    
