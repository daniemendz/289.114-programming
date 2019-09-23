def setup():
    size(800,800)

class Amoeba:
    def __init__(self, x,y, xspeed,yspeed, diameter):
        self.location = PVector(x,y)
        self.velocity = PVector(xspeed, yspeed)
        self.diameter = float(diameter)
        self.wobbleradius = []
        
        for i in range(4):
            self.wobbleradius.append( PVector(
                random(-xspeed*diameter/5, xspeed*diameter/5),
                random(-yspeed*diameter/5, yspeed*diameter/5)
            ))
        
        self.t = 0.0
        
    def ellips(self, x,y,t):
        x = x * cos(t)
        y = y * sin(t)
        return [x,y]
        
    def update(self):
        fill(0x880099ff)
        stroke('#ffffff')
        strokeWeight(3)
        self.location += self.velocity 
        #ellipse(self.location.x,self.location.y, self.diameter,self.diameter)
        
        self.t += 0.05
        d = self.diameter
        r = d/2.0
        c = r*0.552
        e = []
        
        for i in self.wobbleradius:
            xy = self.ellips(i.x,i.y, self.t)
            e.append( PVector(xy[0], xy[1]) )
            
        
        beginShape()
        vertex(
          self.location.x+0, self.location.y+0
        )
        bezierVertex(
          self.location.x+c+e[0].x, self.location.y+e[0].y,
          self.location.x+r+e[1].x, self.location.y+r-c+e[1].x,
          self.location.x+r, self.location.y+r
        )
        bezierVertex(
          self.location.x+r+e[1].x*-1, self.location.y+r+c+e[1].y*-1,
          self.location.x+c+e[2].x, self.location.y+d+e[2].y,
          self.location.x, self.location.y+d
        )
        bezierVertex(
          self.location.x-c+e[2].x*-1, self.location.y+d+e[2].y*-1,
          self.location.x-r+e[3].x, self.location.y+r+c+e[3].y,
          self.location.x-r, self.location.y+r
        )
        bezierVertex(
          self.location.x-r+e[3].x*-1, self.location.y+r-c+e[3].y*-1,
          self.location.x-c+e[0].x*-1, self.location.y+e[0].y*-1,
          self.location.x, self.location.y
        )
        endShape()
        
        '''
        # control points visualized
        stroke('#FF0000')
        strokeWeight(2)
        line(
          self.location.x+c+e[0].x, self.location.y+e[0].y, 
          self.location.x-c+e[0].x*-1, self.location.y+e[0].y*-1
        )
        line(
          self.location.x+r+e[1].x, self.location.y+r-c+e[1].y, 
          self.location.x+r+e[1].x*-1, self.location.y+r+c+e[1].y*-1
        )
        line(
          self.location.x+c+e[2].x, self.location.y+d+e[2].y,
          self.location.x-c+e[2].x*-1, self.location.y+d+e[2].y*-1
        )
        line(
          self.location.x-r+e[3].x, self.location.y+r+c+e[3].y,
          self.location.x-r+e[3].x*-1, self.location.y+r-c+e[3].y*-1
        )
        '''

a = Amoeba(300,200, 0.2,0.2, 150)
b = Amoeba(100,100, 0.4, 0.5, 60)

def draw():
    background('#004477')
    
    a.update()
    b.update()
    
    
