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

    if detEyeRight == -1:
        righteye += 1
        break
    
if righteye == 0: #add white square if none detected
    dER_x = 450
    dER_y = 250
    fill('#ffffff')
    rect(400,200, 100,100)
    righteye += 1    


#mouth position
mouth = 0
for i in range(20): #detects white squares
    dM_xco = [150, 250, 350]
    dM_yco = [350, 450]
    dM_x = dM_xco[int(random(0,3))]
    dM_y = dM_yco[int(random(0,2))]
    detMouth = get(dM_x,dM_y)
    detMouth2 = get(dM_x+100, dM_y)

    if detMouth == -1 and detMouth2 == -1:
        mouth += 1
        break
    
if mouth == 0: #add white square if none detected
    dM_x = 250
    dM_y = 450
    fill('#ffffff')
    rect(200,400, 200,100)
    mouth += 1
    

#place drawings
dEL_x,dEL_y, dER_x,dER_y, dM_x,dM_y = dEL_x-50,dEL_y-50, dER_x-50,dER_y-50, dM_x-50,dM_y-50

print(dEL_x,dEL_y, dER_x,dER_y, dM_x,dM_y)

imgELlist = ['dEL1.png','dEL2.png','dEL3.png']
imgERlist = ['dER1.png','dER2.png','dER3.png']
imgMlist = ['dM1.png','dM2.png','dM3.png']

imgEL = loadImage(imgELlist[int(random(len(imgELlist)))])
image(imgEL, dEL_x,dEL_y)

imgER = loadImage(imgERlist[int(random(len(imgERlist)))])
image(imgER, dER_x,dER_y)

imgM = loadImage(imgMlist[int(random(len(imgMlist)))])
image(imgM, dM_x,dM_y)
