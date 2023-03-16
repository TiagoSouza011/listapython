minha_lista= [1,2,3,4,5]

for i in range(len(minha_lista)):
    print("o elemento", i+1, "da lista é:", minha_lista[i])
    
numeros = [1, 2, 3, 4, 5]
#usando um loop for para percorrer a lista e imprimir cada elemnto
for numero in numeros:
    print(numero, "- com for")
#usando um loop for para percorrer a lista e imprimir cada elemnto
i=0
while i< len(numeros):
    print(numero[i], "- com while")
    i+=1