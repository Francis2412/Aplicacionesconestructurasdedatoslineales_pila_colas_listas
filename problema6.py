#Problema#6 
#Se requiere automatizar un mapa que contiene las estaciones de una ruta previamente 
#establecida para una aplicación que indique, a partir de un punto de la ruta, el tiempo 
#estimado para llegar a un destino determinado de la misma. 

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

def esta_balanceada(expresion: str) -> bool:
    pila = Stack()
    parejas = {')': '(', ']': '[', '}': '{'}
    for simbolo in expresion:
        if simbolo in "([{":
            pila.push(Node(simbolo))
        elif simbolo in ")]}":
            ultimo = pila.pop()
            if ultimo is None or ultimo.data != parejas[simbolo]:
                return False
    return pila.isEmpty()

def main():
    expresion = input("Expresión matemática: ")
    print("Expresión válida" if esta_balanceada(expresion) else "Error de balanceo")

if __name__ == "__main__":
    main()
