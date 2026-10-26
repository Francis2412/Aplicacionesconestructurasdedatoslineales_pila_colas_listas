#Problema#5 
#Torres de Hanoi 
#Dado un conjunto de tres varillas (pilas A, B y C) y discos de tamaño diferente, el objetivo 
#es pasar todos discos de la pila A hacia la pila C, respetando las siguientes 
# reglas: - Solo se puede mover un disco a la vez 
# - Ningún disco puede estar sobre un disco de tamaño menor

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

def mover(origen: Stack, destino: Stack, nombre_origen: str, nombre_destino: str):
    disco = origen.pop()
    if disco is None:
        raise ValueError("La torre de origen está vacía")
    if not destino.isEmpty() and destino.peek() < disco.data:
        origen.push(disco)
        raise ValueError("No se puede poner un disco grande sobre uno pequeño")
    destino.push(disco)
    print(f"Mover disco {disco.data}: {nombre_origen} -> {nombre_destino}")

def hanoi(n, origen, auxiliar, destino, nombre_origen, nombre_auxiliar, nombre_destino):
    if n == 0:
        return
    hanoi(n - 1, origen, destino, auxiliar, nombre_origen, nombre_destino, nombre_auxiliar)
    mover(origen, destino, nombre_origen, nombre_destino)
    hanoi(n - 1, auxiliar, origen, destino, nombre_auxiliar, nombre_origen, nombre_destino)

def main():
    try:
        n = int(input("Cantidad de discos (1 a 10): "))
    except ValueError:
        print("Ingrese un entero")
        return
    if n < 1 or n > 10:
        print("Debe ser de 1 a 10")
        return
    a, b, c = Stack(), Stack(), Stack()
    for disco in range(n, 0, -1):
        a.push(Node(disco))
    hanoi(n, a, b, c, "A", "B", "C")
    print("Completado. Discos en C:", n)

if __name__ == "__main__":
    main()
