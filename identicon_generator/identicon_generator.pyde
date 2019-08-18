size(600,600)
noStroke()

csv = loadStrings('spacewalk_records.csv')
colour = ['#ff8da0', '#55ffc1', '#3febff', '#6c87fe', '#c0a1ff']

col = 0
row = 0

aPick = int(random(1,30))
entry = csv[aPick].split('\t')
number = int(entry[0])
name = entry[1]
agency = entry[2]
eva = int(entry[3])
time = int(entry[4])

nameLen = len( name.replace(' ','').replace('.','') )
randseed = nameLen + eva + time - number
print(number)

if agency == 'NASA':
    randseed = randseed*time*2
else: 
    randseed = randseed/time

randseed+= nameLen
    
if number>24:
    colourPick = 4
elif number>18:
    colourPick = 3
elif number>12:
    colourPick = 2
elif number>6:
    colourPick = 1
else:
    colourPick = 0
    

randomSeed(randseed)


bgcolour = ['#ffffff', colour[colourPick]]


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
for i in range(14): #detects white squares
    dER_xco = [350, 450]
    dER_yco = [150, 250]
    dER_x = dER_xco[int(random(0,2))]
    dER_y = dER_yco[int(random(0,2))]
    detEyeRight = get(dER_x,dEL_y)

    if detEyeRight == -1:
        righteye += 1
        break
    
if righteye == 0: #add white square if none detected
    dER_x = 450
    dER_y = 250
    fill('#ffffff')
    rect(400,dEL_y-50, 100,100)
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
    dM_y = 350
    fill('#ffffff')
    rect(200,300, 200,100)
    mouth += 1
    

#place drawings
dEL_x,dEL_y, dER_x,dER_y, dM_x,dM_y = dEL_x-50,dEL_y-50, dER_x-50,dER_y-50, dM_x-50,dM_y-50

imgELlist = ['dEL1.png','dEL2.png','dEL3.png']
imgERlist = ['dER1.png','dER2.png','dER3.png']
imgMlist = ['dM1.png','dM2.png','dM3.png','dM4.png']

imgEL = loadImage(imgELlist[int(random(len(imgELlist)))])
image(imgEL, dEL_x,dEL_y)

imgER = loadImage(imgERlist[int(random(len(imgERlist)))])
image(imgER, dER_x,dEL_y)

imgM = loadImage(imgMlist[int(random(len(imgMlist)))])
image(imgM, dM_x,dM_y)

#border
beginShape()
fill(colour[colourPick])
noStroke()
vertex(0,0)
vertex(0,600)
vertex(600,600)
vertex(600,0)
vertex(0,0)
#apple
beginContour()
vertex(100,100)
vertex(500,100)
vertex(500,500)
vertex(100,500)
vertex(100,100)
endContour()
endShape() 
