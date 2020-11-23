# def potencia(base):
#     """Documentación"""
#     exponente=1
#     while True:
#         yield base**exponente
#         exponente+=1

# i = 0
# it = potencia(2)
# while i < 100:
#     print(it.__next__())
#     i += 1



def potencia(base, exponente):
    i = 0
    result = 1
    while i < exponente:
        result = base*result
        i += 1
        yield result
    return
    
for i in potencia(2, 3):
    print(i)



