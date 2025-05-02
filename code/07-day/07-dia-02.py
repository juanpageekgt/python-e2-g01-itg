class Node:
    """Clase para representar un nodo de una lista circular enlazada"""
    def __init__(self, data):
        self.data = data # Dato almacenado en el nodo
        self.next = None # Puntero al siguiente nodo


class CircularLinkedList:
    """Clase para manejar una lista circular enlazada"""
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Agrega un nuevo nodo al final de la lista"""
        new_node = Node(data)
        if not self.head: # Si la lista está vacía
            self.head = new_node
            new_node.next = self.head # apunta a sí mismo
            return
        current = self.head
        while current.next != self.head: # recorre hasta el último nodo
            current = current.next
        current.next = new_node
        new_node.next = self.head # El nuvo nodo apunta al primero
    
    def display(self):
        """Muestra los elementos de la lista circular"""
        if not self.head:
            print('Lista vacia')
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head: # si ha vuelto al inicio, detenerse
                break
        print('(circular)')


# Ejemplo de uso
cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)

print('Lista circular:')
cll.display()