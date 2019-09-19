size(600,600)
imgArray = ['00.gif', '01.gif', '02.gif', '03.gif', '04.gif', '05.gif', '06.gif', 
            '07.gif', '08.gif', '09.gif', '10.gif', '11.gif', '12.gif', '13.gif', 
            '14.gif', '15.gif', ]

#green -16711936, yellow -256, red -65536, blue -16737793

col = 0
row = 0

for i in range(1,400):
    
    #first square
    if i == 1:
        pick = int(random(0,16))
        img = loadImage(imgArray[pick])
        img.resize(30,30)
        image(img,col,row)
    
    #first square of next rows
    if i%19==0:
        detTop =  get(15,row+25) #detect colour
        
        if detTop == -65536: #red
            pick = int(random(0,8))
        else: #green
            pick = int(random(8,16))
            
        row+=30
        col = 0
        img = loadImage(imgArray[pick])
        img.resize(30,30)
        image(img,col,row)

    #detect colour
    det = get(col+25,row+15)
    col += 30
    
    #first row
    if row == 0:
        if det == -16737793: # blue
            pick = (int(random(0,16))/2)*2
        elif det == -256: # yellow
            pick = ((int(random(0,15))/2)*2)+1
    
    #remaining rows
    else:
        detTop =  get(col+15,row-5) #detect colour
    
        if detTop == -65536 and det == -16737793: #red blue
            pick = (int(random(0,8))/2)*2
        elif detTop == -16711936 and det == -256: #green yellow
            pick = ((int(random(8,15))/2)*2)+1
        elif detTop == -65536 and det == -256: #red yellow
            pick = ((int(random(0,7))/2)*2)+1
        else:
            pick = (int(random(8,16))/2)*2
    
    img = loadImage(imgArray[pick])
    img.resize(30,30)
    image(img,col,row)
    
        

        
    
    
    
