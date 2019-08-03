size(600,600)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

line(75,138, 228,88)

for i in range(12):
    line(75,138+10*i, 228,88+10*i)

for i in range(1,8):
    x = i**2.5
    line(370,80+x, 522,80+x)
    print(x)
    
