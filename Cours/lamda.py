
# fonction x --> x + 5
f=lambda x:x+5
print(f(3))
#programme qui filtre une liste et affiche les nombres paires
L = [13 , 16 , 22 , 31 , 17 , 46]
out1=list(filter(lambda x:(x%2==0),L))
print(out1)
#programme qui filtre un dictionnaire et affiche les personnes majeurs
d = {'Ahmed' : 15 , 'Robert' : 18 , 'Nathalie': 19 , 'Cecilia' : 13 , 'David' : 14 }
out2=list(filter(lambda x:(d[x] >=18),d))
print(out2)
#programme qui renvoie la liste des carrées des éléments d'une liste
L2 = [11 , 3 , 7 , 2 , 5 , 9]
out3=list(map(lambda x:x*x,L2))
print(out3)