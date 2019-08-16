size(600,600)
noStroke()

colour = ['#ff9494', '#5efec3', '#63faea', '#7589ff', '#bfa3ff']
colourPick = int(random(len(colour)))
bgcolour = ['#ffffff', colour[colourPick]]

col = 0
row = 0

for i in range(36):
    
    bgcolPick = int(random(len(bgcolour)))
    fill(bgcolour[bgcolPick])
    rect(row*100,col*100, 100,100)
    
    '''
    fill(detEyeLeft)
    ellipse(300,300,300,300)
    print(detEyeLeft)
    '''
    
    row += 1
    
    if row%6==0:
        row = 0
        col += 1
    
#left eye position
lefteye = 0
for i in range(8): #detects white squares
    dEL_xco = [150, 250]
    dEL_yco = [150, 250]
    dEL_x = dEL_xco[int(random(0,2))]
    dEL_y = dEL_yco[int(random(0,2))]
    detEyeLeft = get(dEL_x,dEL_y)

    if detEyeLeft == -1:
        lefteye += 1
        break
    
if lefteye == 0: #add white square if none detected
    dEL_x = 150
    dEL_y = 250
    fill('#ffffff')
    rect(100,200, 100,100)
    lefteye += 1

#right eye position
righteye = 0
for i in range(8): #detects white squares
    dER_xco = [350, 450]
    dER_yco = [150, 250]
    dER_x = dER_xco[int(random(0,2))]
    dER_y = dER_yco[int(random(0,2))]
    detEyeRight = get(dER_x,dER_y)
    print(detEyeRight)
    if detEyeRight == -1:
        print('found')
        righteye += 1
        break
    
if righteye == 0: #add white square if none detected
    dER_x = 450
    dER_y = 250
    fill('#ffffff')
    rect(400,200, 100,100)
    righteye += 1    
    print('added')
print(dER_x)
print(dER_y)
    
    
    
    
