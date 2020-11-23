num = int(input('Escribe un número: '))

es_primo = True

for i in range(2, num):
    if num % i == 0:
        es_primo = False
        print('El número no es primo')  
        break
   
if es_primo == True:
    print('El número es primo')

            



