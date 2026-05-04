class Pile:
    def __init__(self):
        print("[Pile] Création d'une nouvelle pile vide.")
        self._items = []

    def pile_vide(self):
        est_vide = len(self._items) == 0
        print(f"[Pile] Vérification si la pile est vide : {est_vide}")
        return est_vide

    def empiler(self, value):
        self._items.append(value)
        print(f"[Pile] Empiler : Ajout de '{value}' au sommet. État de la pile : {self._items}")

    def depiler(self):
        if self.pile_vide():
            print("[Pile] Erreur : Tentative de dépiler une pile vide !")
            raise IndexError("Erreur : Pile vide")
        valeur_retiree = self._items.pop()
        print(f"[Pile] Dépiler : Retrait de '{valeur_retiree}' du sommet. État restant : {self._items}")
        return valeur_retiree

    def rechercher(self, target):
        print(f"[Pile] Recherche de la valeur '{target}'...")
        trouve = target in self._items
        print(f"[Pile] Résultat de la recherche pour '{target}' : {trouve}")
        return trouve


class File:
    def __init__(self):
        print("[File] Création d'une nouvelle file vide.")
        self._items = []

    def file_vide(self):
        est_vide = len(self._items) == 0
        print(f"[File] Vérification si la file est vide : {est_vide}")
        return est_vide

    def ajouter(self, value):
        self._items.append(value)
        print(f"[File] Ajouter : Entrée de '{value}' à la fin de la file. État : {self._items}")

    def retirer(self):
        if self.file_vide():
            print("[File] Erreur : Tentative de retirer d'une file vide !")
            raise IndexError("Erreur : File vide")
        valeur_retiree = self._items.pop(0)
        print(f"[File] Retirer : Sortie de '{valeur_retiree}' au début de la file. État restant : {self._items}")
        return valeur_retiree

    def rechercher(self, target):
        print(f"[File] Recherche de la valeur '{target}'...")
        trouve = target in self._items
        print(f"[File] Résultat de la recherche pour '{target}' : {trouve}")
        return trouve


class Maillon:
    def __init__(self, value):
        print(f"  -> [Maillon] Création d'un nœud pour la valeur '{value}'")
        self.value = value
        self.next = None


class ListeChainee:
    def __init__(self):
        print("[Liste] Création d'une Liste Chaînée vide.")
        self.head = None

    def inserer(self, value):
        print(f"[Liste] Demande d'insertion de la valeur '{value}'...")
        nouveau = Maillon(value)
        
        if self.head is None:
            print(f"[Liste] La liste était vide. '{value}' devient la tête (head).")
            self.head = nouveau
            return

        courant = self.head
        print("[Liste] Parcours des maillons pour trouver la fin...")
        while courant.next is not None:
            courant = courant.next
            
        courant.next = nouveau
        print(f"[Liste] '{value}' a été accroché à la fin de la liste.")

    def supprimer(self, value):
        print(f"[Liste] Tentative de suppression de '{value}'...")
        if self.head is None:
            print("[Liste] La liste est vide, rien à supprimer.")
            return False

        if self.head.value == value:
            print(f"[Liste] '{value}' trouvé à la tête ! On décale la tête au maillon suivant.")
            self.head = self.head.next
            return True

        precedent = self.head
        courant = self.head.next
        
        while courant is not None:
            if courant.value == value:
                print(f"[Liste] '{value}' trouvé ! On relie le maillon précédent directement au suivant (Bypass).")
                precedent.next = courant.next
                return True
            precedent = courant
            courant = courant.next
            
        print(f"[Liste] La valeur '{value}' n'existe pas dans la liste.")
        return False

    def rechercher(self, target):
        print(f"[Liste] Recherche de '{target}' en parcourant les maillons...")
        courant = self.head
        position = 0
        while courant is not None:
            if courant.value == target:
                print(f"[Liste] '{target}' trouvé à la position (index) {position}.")
                return True
            courant = courant.next
            position += 1
            
        print(f"[Liste] '{target}' introuvable après avoir parcouru toute la liste.")
        return False

    def to_list(self):
        values = []
        courant = self.head
        while courant is not None:
            values.append(courant.value)
            courant = courant.next
        return values

