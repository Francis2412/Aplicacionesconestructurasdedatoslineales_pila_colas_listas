#Problema#1 
#Se requiere implementar un sistema que simule las operaciones de deshacer y rehacer 
#acciones en un editor de texto. El programa debe permitir agregar texto, deshacer la última 
#acción realizada y rehacer una acción previamente deshecha, utilizando dos pilas para 
#administrar el historial de acciones. Cuando se realice una nueva acción después de 
#deshacer, se deberá limpiar la pila de rehacer. La solución debe desarrollarse de forma 
#modular en Python, utilizando las operaciones básicas de la estructura de datos Pila. 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self)->bool:
        if self.top == None:
             return True
        else:
            return False

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

def agregar_texto(texto, deshacer, rehacer, nuevo):
    deshacer.push(Node(texto))
    rehacer.clear()
    return texto + nuevo

def deshacer_accion(texto, deshacer, rehacer):
    if deshacer.isEmpty():
        print("No hay acciones para deshacer")
        return texto
    rehacer.push(Node(texto))
    return deshacer.pop().data

def rehacer_accion(texto, deshacer, rehacer):
    if rehacer.isEmpty():
        print("No hay acciones para rehacer")
        return texto
    deshacer.push(Node(texto))
    return rehacer.pop().data

def main():
    deshacer = Stack()
    rehacer = Stack()
    texto = ""
    while True:
        print("***** Menu de opciones *****")
        print("1..............Agregar texto")
        print("2...................Deshacer")
        print("3....................Rehacer")
        print("4..................Ver texto")
        print("5......................Salir")
        opcion = int(input("Opción: "))
        match opcion:
            case 1:
                texto = agregar_texto(texto, deshacer, rehacer, input("Texto a agregar: "))
            case 2: 
                texto = deshacer_accion(texto, deshacer, rehacer)
            case 3:
                texto = rehacer_accion(texto, deshacer, rehacer)
            case 4:
              print("Texto actual:", repr(texto))  
            case 5:
                break
            case 6:
                print("Opción inválida")
        print("Estado:", repr(texto))

main()
