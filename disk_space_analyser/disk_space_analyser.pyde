size(600,700)
background('#004477')
stroke('#FFFFFF')
strokeWeight(3)
noFill()

x = width/2
y = height/2

#arcs uses radians. PI is semicircle.
#arc(x_co, y_co, w_circle,h_circle, start_angle, end_angle)

arc(x,y, 350,350, PI/2,PI , PIE)


fill("#004477")
arc(x,y, 200,200, 0,PI*2 ) 
