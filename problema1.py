#Problema#1 
#Se requiere implementar un sistema que simule las operaciones de deshacer y rehacer 
#acciones en un editor de texto. El programa debe permitir agregar texto, deshacer la última 
#acción realizada y rehacer una acción previamente deshecha, utilizando dos pilas para 
#administrar el historial de acciones. Cuando se realice una nueva acción después de 
#deshacer, se deberá limpiar la pila de rehacer. La solución debe desarrollarse de forma 
#modular en Python, utilizando las operaciones básicas de la estructura de datos Pila. 

class Node:
    def __init__(self, data:str):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def push(self, new: Node):
        if self.isEmpty():
            self.top = new
        else:
            new.next = self.top
            self.top = new

    def pop(self):
        if self.isEmpty():
            return None

        node = Node(self.top.data)
        self.top = self.top.next
        return node

    def agregar_texto(texto, pila_deshacer, pila_rehacer, nuevo):
        pila_deshacer.push(Node(texto))

        texto = texto + nuevo

        while not pila_rehacer.isEmpty():
            pila_rehacer.pop()

        return texto


    def deshacer(texto, pila_deshacer, pila_rehacer):
        if not pila_deshacer.isEmpty():
            pila_rehacer.push(Node(texto))
            texto = pila_deshacer.pop().data
        return texto


    def rehacer(texto, pila_deshacer, pila_rehacer):
        if not pila_rehacer.isEmpty():
            pila_deshacer.push(Node(texto))
            texto = pila_rehacer.pop().data
        return texto