size(600,600)
imgArray = ['00.gif', '01.gif', '02.gif', '03.gif', '04.gif', '05.gif', '06.gif', 
            '07.gif', '08.gif', '09.gif', '10.gif', '11.gif', '12.gif', '13.gif', 
            '14.gif', '15.gif', ]

'''
green -16711936
yellow -256
red -65536
blue -16737793
'''

col = 0
row = 0

pick1 = int(random(0,16))
firstimg = loadImage(imgArray[pick1])
firstimg.resize(30, 30)
image(firstimg, 0,0)

for i in range(20):
    det1 = get(row+25,15)
    strokeWeight(2)
    stroke('#000000')
    point(row+25,15)
    print(det1)
    row+=30
        
    if det1 == -16737793: # blue
        pick = (int(random(0,16))/2)*2
        print(pick)
        img = loadImage(imgArray[pick])
        img.resize(30,30)
        image(img,row,col)
    
    elif det1 == -256: # yellow
        pick = ((int(random(0,15))/2)*2)+1
        print(pick)
        img = loadImage(imgArray[pick])
        img.resize(30,30)
        image(img,row,col)
    
    

    
     



'''
if picker%2==0: # if even, blue side

else: # if odd, yellow side

picker = random(8,16) #green top
picker = random(0,8) #red top


col += 50
if i%20==0:
        row += 50
        col = 0
'''