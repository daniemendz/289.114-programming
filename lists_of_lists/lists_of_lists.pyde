size(500,380)
background('#004477')
noFill()
stroke('#FFFFFFF')
strokeWeight(3)

h = 50
translate(100,40)

# 0 dimensional
bands = 6
rect(0,0, 40,h*bands)

# 1 dimensional
bands = ['#FF0000','#FF9900','#FFFF00','#00FF00', '#0099FF','#6633FF']

for i in range(len(bands)):
    fill(bands[i])
    rect(0,i*h, 40,h)

# 2 dimensional
bands = []
