# from enum import Enum
# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3
# print(Color.RED)  # name
# print(Color.RED.value)


obj = (1,2,3)

# dir()
# hasattr()  # "return whether the object has an attribute with the given name"
# nota: en este contexto, los métodos también son un tipo de atributo y
# por eso al usar hasattr() aparecen también. Podemos "afinar" después
print([x + ": " + str(type(getattr(obj, x))) for x in dir(obj)])
