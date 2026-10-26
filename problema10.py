#Problema#10 
#Un aeropuerto internacional necesita un sistema para organizar el despegue de vuelos 
#nacionales e internacionales. Cada vuelo tiene: código de vuelo, aerolínea, destino y tipo. 
#El sistema debe: ingresar vuelos a la cola, priorizar vuelos de emergencia, autorizar el 
#siguiente vuelo para despegar. 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Cola:
    def __init__(self):
        self.front = None
        self.back = None

    def isEmpty(self):
        return self.front is None

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

class Vuelo:
    def __init__(self, codigo, aerolinea, destino, tipo, emergencia=False):
        self.codigo = codigo
        self.aerolinea = aerolinea
        self.destino = destino
        self.tipo = tipo
        self.emergencia = emergencia

def siguiente_despegue(emergencias, normales):
    if not emergencias.isEmpty():
        return emergencias.dequeue()
    return normales.dequeue()

def main():
    normales = Cola()
    emergencias = Cola()
    while True:
        print("\n1. Registrar vuelo  2. Autorizar despegue  3. Ver siguiente  0. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            codigo = input("Código: ")
            aerolinea = input("Aerolínea: ")
            destino = input("Destino: ")
            tipo = input("Tipo (nacional/internacional): ").strip().lower()
            if tipo not in ("nacional", "internacional"):
                print("Tipo inválido")
                continue
            emergencia = input("¿Emergencia? (s/n): ").lower() == "s"
            vuelo = Vuelo(codigo, aerolinea, destino, tipo, emergencia)
            if emergencia:
                emergencias.enqueue(Node(vuelo))
            else:
                normales.enqueue(Node(vuelo))
        elif opcion == "2":
            nodo = siguiente_despegue(emergencias, normales)
            if nodo:
                v = nodo.data
                print(f"Despegue autorizado: {v.codigo} | {v.aerolinea} | {v.destino} | {v.tipo} | Emergencia: {v.emergencia}")
            else:
                print("No hay vuelos pendientes")
        elif opcion == "3":
            v = emergencias.peek() if not emergencias.isEmpty() else normales.peek()
            print(f"Siguiente: {v.codigo} a {v.destino}" if v else "No hay vuelos pendientes")
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
