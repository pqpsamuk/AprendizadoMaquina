
from math import sqrt
 
def  euclidiana(a, b):
	return sqrt(sum((e1-e2)**2 for e1, e2 in zip(a,b)))
 
carro1 = [1.952, 1.213, 333000]
carro2 = [1.720, 1.940, 23230]

distancia_euclidiana = euclidiana(carro1, carro2)
print(distancia_euclidiana)

def manhattan(a, b):
	return sum(abs(e1-e2) for e1, e2 in zip(a,b))

carro1 = [1.952, 1.213, 333000]
carro2 = [1.720, 1.940, 23230]

distancia_manhattan = manhattan(carro1, carro2)
print(distancia_manhattan)


def minkowski(a, b, p):
	return sum(abs(e1-e2)**p for e1, e2 in zip(a,b))**(1/p)
 
carro1 = [1.952, 1.213, 333000]
carro2 = [1.720, 1.940, 23230]
distancia_minkowski = minkowski(carro1, carro2, 2)
print(distancia_minkowski)

def hamming(Nome1, Nome2):
    i = 0
    count = 0
 
    while(i < len(Nome1)):
        if(Nome1[i] != Nome2[i]):
            count += 1
        i += 1
    return count
 
Nome1 = "Corsa"
Nome2 = "Sedan"
print(hamming(Nome1, Nome2))