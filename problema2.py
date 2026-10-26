#Problema#2 
#Se requiere implementar un método que reciba una pila de enteros como único parámetro, 
#el cual deberá retornar la pila con los números pares en la parte inferior y los impares en 
#la superior. 
#Por ejemplo: 
#Entrada –> [ 2, 3, 6, 8, 11, 13, 18, 21] 
#Salida –> [ 2, 6,z 8, 18, 3, 11, 13, 21] 

class Producto:
    def __init__(self, entero:int):
        
        try:
            num = input(int(("Ingrese la longitud que desea que sea la pila: ")))
        except ValueError:
            print("Debias ingresar un entero")
        
        for i in range(num):
            self.entero = entero
            pila += entero
        