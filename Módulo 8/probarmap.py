def square(number):
    return number*number
numbers = [1,2,3,4,5]

# # Sin map(), forma "sencilla", sería:
# squared_numbers = []
# for number in numbers:
#     squared = square(number)
#     squared_numbers.append(squared)

# Lo mismo del bucle pero con map() sería:
squared_numbers = map(square, numbers