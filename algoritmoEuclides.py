

'''En este programa calculo el MCD entre dos numeros
utilizando el algoritmo de euclides'''

def mcd(a,b):
    if b == 0:
        return a
    else:
        residuo = 0
        x = a // b
        residuo = a - (x * b)
        return mcd(b, residuo)

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
print("\nEl MCD ENTRE " , a , " Y " , b , " ES: ")
print(mcd(a,b))
