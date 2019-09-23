def setup():
    size(800,800)



a = Amoeba(300,200, 0.2,0.2, 150)
b = Amoeba(100,100, 0.4, 0.5, 60)

def draw():
    background('#004477')
    
    a.update()
    b.update()
    
    
