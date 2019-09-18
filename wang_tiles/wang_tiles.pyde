size(600,600)
imgArray = ['00.gif', '01.gif', '02.gif', '03.gif', '04.gif', '05.gif', '06.gif', 
            '07.gif', '08.gif', '09.gif', '10.gif', '11.gif', '12.gif', '13.gif', 
            '14.gif', '15.gif', ]

col = 0
row = 0

picker = int(random(0,16))
firstimg = loadImage(imgArray[picker])
firstimg.resize(30, 30)
image(firstimg, 0,0)

get()

'''
col += 50
if i%20==0:
        row += 50
        col = 0
'''

'''
green -16711936
yellow -256
red -65536
blue -16737793
'''
