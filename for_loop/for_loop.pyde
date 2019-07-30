size(500,500)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

#1 argument for max, 2 for min+max, 3 for min+max+step size. 
for i in range(0, 12, 3): #(24), (0, 12, 3), (8,20) etc
    ellipse(width/2, height/2, 30*i,30*i)
    print(i)
