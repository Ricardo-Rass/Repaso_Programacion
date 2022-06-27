#intercambiar el valor de 2 variables



#Primera Solucion, usando trampa de python

A=input("ingresa numero para 'A':")
B=input("ingresa numero para 'B':")

A,B=B,A

print(f"new value of 'A' is: {A}")
print(f"new value of 'B' is: {B}")



#segunda solucion, SIN trampa de python --------------------------------------------

x=int(input("ingresa numero para 'x':"))
y=int(input("ingresa numero para 'y':"))

x=x-y
y=x+y
x=y-x

print(f"new value of 'x' is: {x}")
print(f"new value of 'y' is: {y}")
