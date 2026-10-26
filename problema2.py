#Problema#2 
#Se requiere implementar un método que reciba una pila de enteros como único parámetro, 
#el cual deberá retornar la pila con los números pares en la parte inferior y los impares en 
#la superior. 
#Por ejemplo: 
#Entrada –> [ 2, 3, 6, 8, 11, 13, 18, 21] 
#Salida –> [ 2, 6,z 8, 18, 3, 11, 13, 21] 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, new: Node):
        new.next = self.top
        self.top = new

    def pop(self):
        if self.isEmpty():
            return None
        node = Node(self.top.data)
        self.top = self.top.next
        return node

    def peek(self):
        if self.isEmpty():
            return None
        return self.top.data

    def clear(self):
        while not self.isEmpty():
            self.pop()

def ordenar_pila(pila: Stack) -> Stack:
    # Se usan pilas auxiliares para conservar el orden original en cada grupo.
    original = Stack()
    pares = Stack()
    impares = Stack()
    while not pila.isEmpty():
        original.push(pila.pop())
    while not original.isEmpty():
        n = original.pop().data
        if n % 2 == 0:
            pares.push(Node(n))
        else:
            impares.push(Node(n))
    while not pares.isEmpty():
        original.push(pares.pop())
    while not original.isEmpty():
        pila.push(original.pop())
    while not impares.isEmpty():
        original.push(impares.pop())
    while not original.isEmpty():
        pila.push(original.pop())
    return pila

def mostrar_de_abajo_arriba(pila):
    auxiliar = Stack()
    while not pila.isEmpty():
        auxiliar.push(pila.pop())
    numeros = []
    while not auxiliar.isEmpty():
        n = auxiliar.pop().data
        numeros.append(n)
        pila.push(Node(n))
    print(numeros)

def main():
    pila = Stack()
    for n in [2, 3, 6, 8, 11, 13, 18, 21]:
        pila.push(Node(n))
    print("Entrada (abajo a arriba):")
    mostrar_de_abajo_arriba(pila)
    ordenar_pila(pila)
    print("Salida (abajo a arriba):")
    mostrar_de_abajo_arriba(pila)

main()