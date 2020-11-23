def print_all_after_delete_first(l):
    del l[0]
   
lista = [1, 2, 3, 4, 5, 6]
print_all_after_delete_first(lista)
print(lista)

def print_delete_first(l):
    copia_lista = lista[:]
    del l[0]
    print(lista)
    print(copia_lista)
    
   
lista = [1, 2, 3, 4, 5, 6]
print_delete_first(lista)
print_all_after_delete_first(lista)


