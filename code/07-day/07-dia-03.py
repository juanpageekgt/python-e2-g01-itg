class Node:
    """Clase para representar una lista doblemente enlazada circular"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    """clase para manejar una lista circular doblemente enlazada"""
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Agrega un nuevo nodo al final de la lista"""
        new_node = Node(data)
        if not self.head: # si la lista está vacía
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
            return
        last = self.head.prev # el último nodo
        last.next = new_node
        new_node.prev = last
        new_node.next = self.head
        self.head.prev = new_node
    
    def display(self):
        """muestra los elementos de la lista circular doblemente enlazada"""
        if not self.head:
            print('Lista vacia')
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print('(circular)')

# Ejemplo de uso
cdll = CircularDoublyLinkedList()
cdll.append(10)
cdll.append(20)
cdll.append(30)

print('Lista Circular doblemente enlazada')
cdll.display()