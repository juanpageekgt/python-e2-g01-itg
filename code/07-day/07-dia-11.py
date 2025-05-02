class Node:
    """Clase para representar un nodo del árbol Rojo-Negro."""
    def __init__(self, data):
        self.data = data
        self.color = 'RED'  # Cada nuevo nodo se inserta como rojo por defecto
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    """Clase para manejar un árbol Rojo-Negro."""
    def __init__(self):
        self.TNULL = Node(0)  # Nodo nulo (hoja negra)
        self.TNULL.color = 'BLACK'
        self.root = self.TNULL

    def insert(self, key):
        """Inserta un nuevo nodo en el árbol Rojo-Negro."""
        new_node = Node(key)
        new_node.left = self.TNULL
        new_node.right = self.TNULL
        new_node.parent = None

        # Paso 1: Inserción en el árbol binario de búsqueda
        parent = None
        current = self.root

        while current != self.TNULL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:  # El árbol estaba vacío
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        # Paso 2: Balancear el árbol después de la inserción
        self.fix_insert(new_node)

    def fix_insert(self, node):
        """Corrige la violación de las propiedades del árbol Rojo-Negro."""
        while node.parent and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:  # El padre está en el lado izquierdo
                uncle = node.parent.parent.right
                if uncle.color == 'RED':  # Caso 1: El tío es rojo
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:  # Caso 2: El nodo es el hijo derecho
                        node = node.parent
                        self.rotate_left(node)
                    # Caso 3: El nodo es el hijo izquierdo
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.rotate_right(node.parent.parent)
            else:  # Simétrico: El padre está en el lado derecho
                uncle = node.parent.parent.left
                if uncle.color == 'RED':  # Caso 1: El tío es rojo
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:  # Caso 2: El nodo es el hijo izquierdo
                        node = node.parent
                        self.rotate_right(node)
                    # Caso 3: El nodo es el hijo derecho
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.rotate_left(node.parent.parent)
        
        self.root.color = 'BLACK'

    def rotate_left(self, node):
        """Rotación a la izquierda."""
        temp = node.right
        node.right = temp.left
        if temp.left != self.TNULL:
            temp.left.parent = node
        temp.parent = node.parent
        if node.parent is None:
            self.root = temp
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp
        temp.left = node
        node.parent = temp

    def rotate_right(self, node):
        """Rotación a la derecha."""
        temp = node.left
        node.left = temp.right
        if temp.right != self.TNULL:
            temp.right.parent = node
        temp.parent = node.parent
        if node.parent is None:
            self.root = temp
        elif node == node.parent.right:
            node.parent.right = temp
        else:
            node.parent.left = temp
        temp.right = node
        node.parent = temp

    def inorder_traversal(self, node):
        """Recorrido inorden del árbol (izquierda, raíz, derecha)."""
        if node != self.TNULL:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

# Ejemplo de uso
rbt = RedBlackTree()

# Insertar elementos
keys = [20, 15, 25, 10, 5, 30]
for key in keys:
    rbt.insert(key)

print("Recorrido inorden del árbol Rojo-Negro:")
rbt.inorder_traversal(rbt.root)
# Salida: 5 10 15 20 25 30