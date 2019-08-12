size(800,800)
background('#004477')
noStroke()

csv = loadStrings('list_of_best-selling_video_games.csv')

tetrisentry = csv[1].split('\t') #split sets delimiter
print(int(tetrisentry[1]) + 1) 
