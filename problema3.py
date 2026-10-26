#Problema#3 
#Un puesto de atención al cliente cuenta con un sistema de cola automática, el cual genera 
#un número consecutivo entre 1 y 10 para organizar la atención a sus clientes. Se requiere 
#optimizar su algoritmo de forma que el administrador del sistema pueda eliminar de la cola 
#a los clientes que abandonan el recinto sin ser atendidos y de esta manera minimizar el 
#tiempo de espera. 

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

def eliminar_cliente(cola: Cola, numero: int) -> bool:
    anterior = None
    actual = cola.front
    while actual is not None:
        if actual.data == numero:
            if anterior is None:
                cola.front = actual.next
            else:
                anterior.next = actual.next
            if actual is cola.back:
                cola.back = anterior
            return True
        anterior = actual
        actual = actual.next
    return False

def mostrar(cola):
    actual = cola.front
    datos = []
    while actual is not None:
        datos.append(actual.data)
        actual = actual.next
    print("Cola:", datos)

def main():
    cola = Cola()
    for numero in range(1, 11):
        cola.enqueue(Node(numero))
    while True:
        mostrar(cola)
        print("1. Cliente abandona  2. Atender siguiente  0. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            try:
                numero = int(input("Número de turno a eliminar (1-10): "))
                print("Eliminado" if eliminar_cliente(cola, numero) else "No encontrado")
            except ValueError:
                print("Debe ingresar un número")
        elif opcion == "2":
            nodo = cola.dequeue()
            print("Atendido:", nodo.data if nodo else "No hay clientes")
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
