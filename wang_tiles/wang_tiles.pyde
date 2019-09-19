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

for i in range(19):
    det = get(col+25,row+15)
    strokeWeight(2)
    stroke('#000000')
    point(col+25,row+15)
    print(det)
    col+=30
    
    if row == 0:
        if det == -16737793: # blue
            pick = (int(random(0,16))/2)*2
        
        elif det == -256: # yellow
            pick = ((int(random(0,15))/2)*2)+1
    
    else:
        random(2)
        
    
        
    img = loadImage(imgArray[pick])
    img.resize(30,30)
    image(img,col,row)


    
     



'''
if picker%2==0: # if even, blue side

else: # if odd, yellow side

picker = random(8,16) #green top
picker = random(0,8) #red top

if i%20==0:
    col += 30
    row = 0
'''
