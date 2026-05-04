from tree_api import BinaryTree
from linear_api import Pile, File, ListeChainee
from matrix_api import (
    create_matrix_5x4,
    create_matrix,
    add_matrices,
    subtract_matrices,
    multiply_matrices,
    calculate_matrix_operation,
)

def test_trees():
    print("\n--- TEST API ARBRES ---")
    tree = BinaryTree.create_with_n_nodes([50, 30, 70, 20, 40, 15, 25])
    
    print("Infixe (trié) :", tree.inorder_traversal())
    print("Préfixe :      ", tree.preorder_traversal())
    print("Postfixe :     ", tree.postorder_traversal())
    print("Largeur (BFS) :", tree.level_order_traversal())




def test_linear_structures():
    print("\n===========================================")
    print("--- DÉBUT DU TEST API LINÉAIRE ---")
    print("===========================================\n")

    print(">>> TEST DE LA PILE (LIFO) <<<")
    pile = Pile()
    pile.empiler(1)
    pile.empiler(2)
    pile.pile_vide()
    pile.rechercher(1)
    pile.depiler()

    print("\n>>> TEST DE LA FILE (FIFO) <<<")
    file = File()
    file.ajouter(10)
    file.ajouter(20)
    file.file_vide()
    file.rechercher(20)
    file.retirer()

    print("\n>>> TEST DE LA LISTE CHAÎNÉE <<<")
    liste = ListeChainee()
    liste.inserer("A")
    liste.inserer("B")
    liste.inserer("C")
    print(f"\n[Aperçu] Liste actuelle : {liste.to_list()}\n")
    
    liste.rechercher("B")
    liste.rechercher("Z")
    liste.supprimer("B")
    
    print(f"\n[Aperçu] Liste après suppression : {liste.to_list()}\n")


def test_matrices():
    print("\n--- TEST API MATRICES ---")

    matrix_5x4 = create_matrix_5x4(1)
    print("Matrice 5x4 :", matrix_5x4)

    a = create_matrix(2, 2)
    b = create_matrix(2, 2)
    a[0][0], a[0][1], a[1][0], a[1][1] = 1, 2, 3, 4
    b[0][0], b[0][1], b[1][0], b[1][1] = 5, 6, 7, 8

    print("Addition :", add_matrices(a, b))
    print("Soustraction :", subtract_matrices(a, b))
    print("Multiplication :", multiply_matrices(a, b))
    print("Calcul standard (+) :", calculate_matrix_operation("+", a, b))

if __name__ == "__main__":
    test_trees()
    test_linear_structures()
    test_matrices()