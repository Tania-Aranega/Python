def f1(l): return l[0]
def f2(s): return s.upper()
# def f_comp(primero, segundo, x):
#     intermedio = primero(x)
#     final = segundo(intermedio)
#     return final  # o directamente: segundo(primero(x))

# print(f_comp(f1, f2, ['hola', 'adiós']))

##AQUÍ BIEN HECHO CON LAMBDA

def f_comp_creator(primero, segundo):
    # devolvemos una función!
    f = lambda x: segundo(primero(x))
    return f

f_comp_creator(f1, f2)('hola')
# lo mismo pero dándole un mombre y en dos pasos:
new_func = f_comp_creator(f1, f2)
new_func('hola')