class Node:
    """Clase para representar un nodo de la lista enlzada"""
    def __init__(self,data):
        self.data = data # Dato almacenado en el nodo
        self.next = None # Puntero al siguiente nodo


class LinkedList:
    """Clase para manejar la lista enlazada."""
    def __init__(self):
        self.head = None #inicialmente, la lista esta vacía

    def append(self, data):
        """Agrega un nuevo nodo al final de la lista."""
        new_node = Node(data)
        if not self.head: # si la lista está vacía
            self.head = new_node
            return
        current = self.head
        while current.next: # Recorre hasta el último nodo
            current = current.next
        current.next = new_node
    
    def display(self):
        """Muestra los elementos de la lista."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Ejemplo de uso
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.display()
