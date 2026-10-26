#Problema#7 
#Un negocio de sorteos requiere un algoritmo para obtener tres números ganadores. Cada 
#número ganador consta de 3 dígitos, los cuales son extraídos de una cola. La cola a su 
#vez se completa de números aleatorios generados por el algoritmo. Cada vez que se 
#genera un número ganador, la cola se rellena con nuevos números aleatorios. 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Cola:
    def __init__(self):
        self.front = None
        self.back = None

    def isEmpty(self) -> bool:
        if self.front == None:
            return True
        else:
            return False

    def enqueue(self, new: Node):
        new.next = None
        if self.front is None:
            self.front = new
            self.back = new
        else:
            self.back.next = new
            self.back = new

    def dequeue(self):
        if self.front is None:
            return None
        node = Node(self.front.data)
        self.front = self.front.next
        if self.front is None:
            self.back = None
        return node

    def peek(self):
        if self.front is None:
            return None
        return self.front.data

    def clear(self):
        while not self.isEmpty():
            self.dequeue()

import random

def llenar_cola(cola: Cola, cantidad=9):
    for _ in range(cantidad):
        cola.enqueue(Node(random.randint(0, 9)))

def obtener_ganador(cola: Cola) -> str:
    digitos = ""
    for _ in range(3):
        nodo = cola.dequeue()
        if nodo is None:
            raise ValueError("No hay suficientes dígitos")
        digitos += str(nodo.data)
    return digitos

def main():
    cola = Cola()
    llenar_cola(cola)
    for i in range(1, 4):
        ganador = obtener_ganador(cola)
        print(f"Ganador {i}: {ganador}")
        llenar_cola(cola, 3)  # Reponer los 3 dígitos extraídos

if __name__ == "__main__":
    main()
