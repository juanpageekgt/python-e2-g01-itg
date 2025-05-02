class TreeNode:
    """Clase para representar un nodo del árbol AVL."""
    def __init__(self, key):
        self.key = key
        self.height = 1  # Altura inicial del nodo
        self.left = None  # Hijo izquierdo
        self.right = None  # Hijo derecho

class AVLTree:
    """Clase para manejar un árbol AVL."""
    def get_height(self, node):
        """Obtiene la altura de un nodo."""
        return node.height if node else 0

    def get_balance(self, node):
        """Calcula el factor de balance de un nodo."""
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        """Rotación simple a la derecha."""
        x = y.left
        T2 = x.right

        # Realizar rotación
        x.right = y
        y.left = T2

        # Actualizar alturas
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def rotate_left(self, x):
        """Rotación simple a la izquierda."""
        y = x.right
        T2 = y.left

        # Realizar rotación
        y.left = x
        x.right = T2

        # Actualizar alturas
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, node, key):
        """Inserta un nodo en el árbol AVL y lo balancea."""
        # Paso 1: Realizar la inserción estándar de un BST
        if not node:
            return TreeNode(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # Paso 2: Actualizar la altura del nodo actual
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Paso 3: Obtener el factor de balance del nodo para verificar si está balanceado
        balance = self.get_balance(node)

        # Caso LL (Rotación a la derecha)
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        # Caso RR (Rotación a la izquierda)
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Caso LR (Rotación izquierda-derecha)
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Caso RL (Rotación derecha-izquierda)
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def inorder_traversal(self, node):
        """Recorrido inorden del árbol (izquierda, raíz, derecha)."""
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

# Ejemplo de uso
avl = AVLTree()
root = None

# Insertar nodos
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = avl.insert(root, key)

print("Recorrido inorden del árbol AVL:")
avl.inorder_traversal(root)
# Salida: 10 20 25 30 40 50