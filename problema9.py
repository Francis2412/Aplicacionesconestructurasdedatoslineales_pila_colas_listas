#problema#9 
#Cree un sistema que simule la atención de llamadas en un Call Center. Cada llamada 
#debe ingresar a una cola con datos como el nombre del cliente y el motivo de la llamada. 
#A medida que los agentes estén disponibles, se debe atender al siguiente cliente en orden 
#de llegada. 

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

class Llamada:
    def __init__(self, cliente, motivo):
        self.cliente = cliente
        self.motivo = motivo

def main():
    cola = Cola()
    while True:
        print("\n1. Recibir llamada  2. Agente disponible  3. Ver siguiente  0. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            cliente = input("Nombre del cliente: ")
            motivo = input("Motivo: ")
            cola.enqueue(Node(Llamada(cliente, motivo)))
        elif opcion == "2":
            nodo = cola.dequeue()
            if nodo:
                print(f"Atendiendo a {nodo.data.cliente}: {nodo.data.motivo}")
            else:
                print("No hay llamadas")
        elif opcion == "3":
            llamada = cola.peek()
            print(f"Siguiente: {llamada.cliente}" if llamada else "No hay llamadas")
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
