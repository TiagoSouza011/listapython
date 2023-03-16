lista_com_duplicates = [1,2,3,1,4,2,5,6,3,7,8,9]

lista_sem_duplicates = []

while lista_com_duplicates:
    elemento = lista_com_duplicates.pop(0)
    if elemento not  in lista_sem_duplicates:
        lista_sem_duplicates.append(elemento)
        
    
print("A lista sem duplicatas é:" , lista_sem_duplicates)