class Node:
    """Clase para representar un node una lista doblemente enlazada"""
    def __init__(self, data):
        self.data = data # Data almacenado en el nodo
        self.next = None # Puntero al siguiente nodo
        self.prev = None # Puntero al nodo anterior


class DoublyLinkedList:
    """Clase para manejar una lista doblemente enlazada"""
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Agrega un nuevo nodo al final de la lista"""
        new_node = Node(data)
        if not self.head: # Si la lista está vacía
            self.head = new_node
            return
        current = self.head
        while current.next: # Recorre hasta el último nodo
            current = current.next
        current.next = new_node
        new_node.prev = current
    
    def display_forward(self):
        """Muestra los elementos de la lista en orden hacia adelante"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print('None')
    
    def display_backward(self):
        """Muestra los elementos de la lista en orden hacía atrás"""
        current = self.head
        if not current:
            print('None')
            return
        while current.next: # Ir al último nodo
            current = current.next
        while current: # Recorrer hacía átras
            print(current.data, end=" -> ")
            current = current.prev
        print('None')


# Ejemplo de uso
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

print('Lista hacia adelante:')
dll.display_forward()

print()

print('Lista hacia atras:')
dll.display_backward()