size(200,200)


def sayHello(firstname, surname):
    print('hello ' + firstname + ' ' + surname)

sayHello('tom', 'smith')
sayHello('zoe', 'jones')
sayHello('sam', 'colins')

def circle(x, y, r): # how processing works essentially, no circle() def in this version of processing
    ellipse(x, y, r, r)
circle(20,20, 20)
