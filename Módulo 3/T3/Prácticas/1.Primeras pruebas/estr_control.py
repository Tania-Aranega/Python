xstr = (input("Dame un numero a:"))
a = float(xstr)
xstr = (input("Dame un numero b:"))
b = float(xstr)
xstr = (input("Dame un numero c:"))
c = float(xstr)

discrim = b * b - (4 * a * c)

if discrim < 0:
    print("Error, no hay números reales")
else:
    x1 = ( (-b) + discrim ** 0.5 ) / (2 * a)
    x2 = ( (-b) - discrim ** 0.5) / (2 * a)
    if x1 == x2:
        print("La solución única (doble) es:", x1)
    else:
    print ('Solución 1:', x1)
    print ('Solución 2:', x2)