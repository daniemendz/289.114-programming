size(800,800)
background('#004477')
noStroke()

csv = loadStrings('list_of_best-selling_video_games.csv')

'''
tetrisentry = csv[1].split('\t') #split sets delimiter
#print(int(tetrisentry[1]) + 1) 
tetrissales = tetrisentry[1]
print( tetrissales )
#print( int(tetrissales) + 1 )
fscale = 800/170000000
#0.00000471
'''

col = 0

for i in range(1,len(csv)):
    entry = csv[i].split('\t')
    sales = entry[1]
    title = entry[2]

    
    fscale = 0.00000471
    fwidth = float(fscale)*float(sales)

    print(float(width))

    fill('#ffffff')
    rect(0,col*16, fwidth,16)
    
    col +=1
    
    
