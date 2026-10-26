#roblema#8 
#Simule el funcionamiento de una cola de impresión en una oficina donde varios empleados 
#envían documentos para ser impresos. Cada documento tiene un nombre, el usuario que 
#lo envió y el número de páginas. El sistema debe permitir agregar documentos a la cola, 
#procesarlos en orden de llegada y mostrar cuál es el documento que se está imprimiendo 
#actualmente. Analice con los estudiantes cómo se evita el desorden en el uso compartido 
#de un recurso limitado. 

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

class Documento:
    def __init__(self, nombre, usuario, paginas):
        self.nombre = nombre
        self.usuario = usuario
        self.paginas = paginas

def main():
    cola = Cola()
    while True:
        print("\n1. Enviar documento  2. Imprimir siguiente  3. Ver siguiente  0. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            nombre = input("Documento: ")
            usuario = input("Empleado: ")
            try:
                paginas = int(input("Páginas: "))
                if paginas <= 0:
                    print("Páginas debe ser mayor que cero")
                    continue
            except ValueError:
                print("Páginas inválidas")
                continue
            cola.enqueue(Node(Documento(nombre, usuario, paginas)))
        elif opcion == "2":
            nodo = cola.dequeue()
            if nodo:
                d = nodo.data
                print(f"Imprimiendo {d.nombre} de {d.usuario} ({d.paginas} páginas)")
            else:
                print("No hay documentos")
        elif opcion == "3":
            d = cola.peek()
            print(f"Siguiente: {d.nombre} de {d.usuario}" if d else "Cola vacía")
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
