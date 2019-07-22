size(500,500)
background('#004477')
fill('#FFFFFF')

#print(PFont.list())
font = createFont('Futura-Medium', 20) #can instead link file eg 'futura.ttf'
textFont(font)

textSize(20)
text('what\'s that?'+' it\'s a knife.'.upper()+" NO", 0,50)
