class TreeNode:
    """Clase para representar un nodo de un árbol binario."""
    def __init__(self, data):
        self.data = data  # Dato almacenado en el nodo
        self.left = None  # Hijo izquierdo
        self.right = None  # Hijo derecho

class BinaryTree:
    """Clase para manejar un árbol binario."""
    def __init__(self):
        self.root = None  # Inicialmente, el árbol está vacío

    def insert(self, data):
        """Inserta un nuevo nodo en el árbol de forma recursiva."""
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursively(self.root, data)

    def _insert_recursively(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursively(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursively(node.right, data)

    def inorder_traversal(self, node):
        """Recorrido inorden del árbol (izquierda, raíz, derecha)."""
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

# Ejemplo de uso
binary_tree = BinaryTree()
binary_tree.insert(50)
binary_tree.insert(30)
binary_tree.insert(70)
binary_tree.insert(20)
binary_tree.insert(40)
binary_tree.insert(60)
binary_tree.insert(80)

print("Recorrido inorden del árbol:")
binary_tree.inorder_traversal(binary_tree.root)
# Salida: 20 30 40 50 60 70 80