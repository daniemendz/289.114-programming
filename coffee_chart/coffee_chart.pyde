size(800,800)
background('#004477')

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
  { 'name':'macchiato',     'espresso':40, 'hotwater':0, 'steamedmilk':60,'foamedmilk':0  },
  { 'name':'flat white',    'espresso':40, 'hotwater':0, 'steamedmilk':0, 'foamedmilk':60  },
]

for coffee in coffees:
    coffee['hotwater']
    coffee['steamedmilk']
    coffee['foamedmilk']

    x = width/4*col
    y = height/4*row
    level = 0
    
    #espresso
    noStroke()
    fill('#332222')
    rect(x-mug/2, y+mug/2-coffee['espresso'], mug,coffee['espresso'])
    level += coffee['espresso']
    
    #hot water
    fill('#0099ff')
    rect(x-mug/2, y+mug/2-coffee['hotwater']-level, mug,coffee['hotwater'])
    level += coffee['hotwater']
    
    #steamed milk
    fill('#ffffff')
    rect(x-mug/2, y+mug/2-coffee['steamedmilk']-level, mug,coffee['steamedmilk'])
    level += coffee['steamedmilk']
    
    #foamed milk
    fill('#dddddd')
    rect(x-mug/2, y+mug/2-coffee['foamedmilk']-level, mug,coffee['foamedmilk'])
    level += coffee['foamedmilk']
    
    #mug
    stroke('#FFFFFF')
    strokeWeight(4)
    noFill()
    arc(x+55,y, 40,40, -HALF_PI,HALF_PI)
    arc(x+55,y, 65,65, -HALF_PI,HALF_PI)
    rect(x-mug/2, y-mug/2, mug,mug)
    
    if col%3==0:
        row += 1
        col = 1
    else:
        col +=1
