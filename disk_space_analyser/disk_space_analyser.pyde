size(600,700)
background('#004477')
stroke('#FFFFFF')
strokeWeight(3)

x = width/2
y = height/2

#arcs uses radians. PI is semicircle.
#arc(x_co, y_co, w_circle,h_circle, start_angle, end_angle)

#third
fill("#00ff00")#green
arc(x,y, 600,600, PI*1.6,PI*1.725, PIE)

#second
fill("#ff96ff")#pink
arc(x,y, 450,450, PI,PI*1.3, PIE)

fill("#ff96ff")
arc(x,y, 450,450, PI*1.3,PI*1.6, PIE)

fill("#0096ff")#blue
arc(x,y, 450,450, PI*1.6,PI*1.85, PIE)

fill("#0096ff")
arc(x,y, 450,450, PI*1.85,PI*2, PIE)

#first 
fill("#6620ff")#magenta
arc(x,y, 300,300, PI*1.6,PI*2, PIE)

fill("#ff2b99")#indigo
arc(x,y, 300,300, PI,PI*1.6, PIE)

fill("#FF0000")#red
arc(x,y, 300,300, 0,PI , PIE)

#center
fill("#004477")
arc(x,y, 150,150, 0,PI*2 ) 
