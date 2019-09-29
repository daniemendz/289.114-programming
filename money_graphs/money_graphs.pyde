size(800,400)
background('#fdbf2d')
stroke('#fd8024')
strokeWeight(4)

csv = loadStrings('the-number-of-new-book-titles-published.csv')

for i in range(1,len(csv)):
    entry = csv[i].split(',')
    x = int(entry[2])-1500 #years
    y = entry[3] #published
    print(x)
