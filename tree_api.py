# tree_api.py

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    @classmethod
    def create_with_n_nodes(cls, values):
        """Crée un arbre binaire de recherche à partir d'une séquence de valeurs."""
        tree = cls()
        for value in values:
            tree.insert(value)
        return tree
    
    def insert(self, value):
        """Insère une valeur en maintenant l'arbre h-équilibré (AVL).
        """
        # Délégué à la version récursive qui retourne la nouvelle racine
        self.root = self._insert_recursive(self.root, value)
        # afficher l'arbre à chaque insertion pour débogage/visualisation
        self.pretty_print()
    
    def _insert_recursive(self, node, value):
        """Insère ``value`` à partir de ``node`` et rééquilibre l'arbre.
        """

        # 1. insertion normale BST
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)

        # 2. mise à jour de la hauteur et calcul du facteur d'équilibre
        balance = self._get_balance(node)

        # cas déséquilibrés : 4 situations classiques AVL
        # gauche-gauche
        if balance > 1 and value < node.left.value:
            return self._rotate_right(node)

        # droite-droite
        if balance < -1 and value > node.right.value:
            return self._rotate_left(node)

        # gauche-droite
        if balance > 1 and value > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # droite-gauche
        if balance < -1 and value < node.right.value:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # --- méthodes utilitaires pour AVL ---
    def _get_height(self, node):
        """Retourne la hauteur d'un nœud (0 si None)."""
        if node is None:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _get_balance(self, node):
        """Facteur d'équilibre = hauteur gauche - hauteur droite."""
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        """Rotation gauche autour du nœud z."""
        y = z.right
        T2 = y.left

        # effectuer rotation
        y.left = z
        z.right = T2

        return y

    def _rotate_right(self, z):
        """Rotation droite autour du nœud z."""
        y = z.left
        T3 = y.right

        # effectuer rotation
        y.right = z
        z.left = T3

        return y

    # --- LES PARCOURS (Demandés par le syllabus) ---

    def inorder_traversal(self, node=None, res=None):
        """Parcours INFIXE : renvoie une liste [gauche, racine, droite]"""
        if res is None: res = []
        if node is None: node = self.root
        
        if node:
            if node.left: self.inorder_traversal(node.left, res)
            res.append(node.value)
            if node.right: self.inorder_traversal(node.right, res)
        return res

    def preorder_traversal(self, node=None, res=None):
        """Parcours PRÉFIXE : renvoie une liste [racine, gauche, droite]"""
        if res is None: res = []
        if node is None: node = self.root
        
        if node:
            res.append(node.value)
            if node.left: self.preorder_traversal(node.left, res)
            if node.right: self.preorder_traversal(node.right, res)
        return res

    def postorder_traversal(self, node=None, res=None):
        """Parcours POSTFIXE : renvoie une liste [gauche, droite, racine]"""
        if res is None: res = []
        if node is None: node = self.root
        
        if node:
            if node.left: self.postorder_traversal(node.left, res)
            if node.right: self.postorder_traversal(node.right, res)
            res.append(node.value)
        return res

    def level_order_traversal(self):
        """Parcours en largeur (BFS)."""
        if self.root is None:
            return []

        result = []
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            result.append(current.value)

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

        return result

    def insert_leaf(self, value):
        """Insertion d'une feuille (alias de l'insertion standard BST)."""
        self.insert(value)

    def insert_branch(self, parent_value, branch_values, side="left"):
        """Insère une branche sous un parent existant, côté gauche ou droit."""
        parent = self._find(self.root, parent_value)
        if parent is None:
            raise ValueError("Parent introuvable dans l'arbre")

        if side not in ("left", "right"):
            raise ValueError("Le paramètre side doit valoir 'left' ou 'right'")

        if not branch_values:
            return

        branch_root = Node(branch_values[0])
        current = branch_root
        for value in branch_values[1:]:
            current.left = Node(value)
            current = current.left

        if side == "left":
            if parent.left is not None:
                raise ValueError("Le parent possède déjà un enfant gauche")
            parent.left = branch_root
        else:
            if parent.right is not None:
                raise ValueError("Le parent possède déjà un enfant droit")
            parent.right = branch_root

    def _find(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        if value < node.value:
            return self._find(node.left, value)
        return self._find(node.right, value)

    # --- utilitaires d'affichage ---
    def pretty_print(self, node=None, prefix="", is_left=True):
        """Affiche l'arbre de manière lisible en ASCII.
        """
        if node is None:
            node = self.root
            # cas d'arbre vide
            if node is None:
                print("(empty tree)")
                return

        # afficher sous-arbre droit d'abord (pour être au-dessus)
        if node.right:
            self.pretty_print(node.right,
                              prefix + ("│   " if is_left else "    "),
                              False)

        # afficher le noeud courant
        connector = "└── " if is_left else "┌── "
        print(prefix + connector + str(node.value))

        # puis sous-arbre gauche
        if node.left:
            self.pretty_print(node.left,
                              prefix + ("    " if is_left else "│   " ),
                              True)