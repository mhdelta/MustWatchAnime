import random as rnd

text = open('animeList.txt', 'r')
animes =  text.read().split('\n')

anime = animes[rnd.randint(0, len(animes))]

print 'Now, you should watch ' + anime
