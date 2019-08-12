size(800,800)

mug = 110
col = 1
row = 1

coffees = [
  { 'name':'cafe con leche','espresso':50, 'hotwater':0, 'steamedmilk':30,'foamedmilk':0  },
  { 'name':'espresso',      'espresso':60, 'hotwater':0, 'steamedmilk':0, 'foamedmilk':0  },
  { 'name':'demi-creme',    'espresso':40, 'hotwater':0, 'steamedmilk':40,'foamedmilk':0  },
  { 'name':'americano',     'espresso':60, 'hotwater':30,'steamedmilk':0, 'foamedmilk':0  },
  { 'name':'capucchino',    'espresso':40, 'hotwater':0, 'steamedmilk':30,'foamedmilk':30 },
  { 'name':'latte',         'espresso':35, 'hotwater':0, 'steamedmilk':10,'foamedmilk':30 },
  { 'name':'ristretto',     'espresso':30, 'hotwater':0, 'steamedmilk':0, 'foamedmilk':0  },
]

for coffee in coffees:
    coffeee['espresso']
    coffeee['hotwater']
    coffeee['steamedmilk']
    coffeee['ffoamedmilk']

    x = width/4*col
    y = height/4*row
    
    stroke('#FFFFFF')
    strokeWeight(4)
    noFill()
    arc(x+55,y, 40,40, -HALF_PI,HALF_PI)
    arc(x+55,y, 65,65, -HALF_PI,HALF_PI)
    
    if col%3==0:
        row += 1
        col = 1
    else:
        col +=1
