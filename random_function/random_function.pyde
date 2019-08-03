randomSeed(213) #optional, but determines what the 'random' output lookslike
size(600,600)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

'''
x = random(5)
print(x)
x = random(5,10)
print(x)
print( int(x) )
'''

for i in range(1000):
    point( random(width), random(height) )
