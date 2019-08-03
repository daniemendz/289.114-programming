size(600,600)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

'''
arc(0,0, 50,50, 0,PI/2)
arc(50,50, 50,50, PI,PI+PI/2)
'''

col = 0
row = 0

for i in range(1,145):
    arc(col,row, 50,50, 0,PI/2)
    arc(col+50,row+50, 50,50, PI,PI+PI/2)
    col += 50

    if i%12 == 0:
        row += 50
        col = 0
