"""
Petit programme complet pour le chiffrement Rail Fence à k niveaux.

Nouveauté pour impressionner le professeur :
- En plus de chiffrer/déchiffrer, le programme peut AFFICHER le texte
  en forme de zigzag (visualisation des rails).
"""

from typing import List


def generer_pattern_indices(longueur: int, k: int) -> List[int]:
    """Génère la liste des indices de ligne (0, 1, ..., k-1) pour chaque
    caractère du texte, en suivant un mouvement en zigzag.

    Exemple pour k = 3 :
        lignes : 0 -> 1 -> 2 -> 1 -> 0 -> 1 -> 2 -> ...

    Si longueur = 7, on obtient : [0, 1, 2, 1, 0, 1, 2]
    """
    if k <= 1:
        return [0] * longueur

    indices: List[int] = []
    ligne = 0          # on commence sur la ligne du haut (0)
    direction = 1      # 1 = on descend, -1 = on remonte

    for _ in range(longueur):
        indices.append(ligne)

        if ligne == 0:
            direction = 1       # en haut -> on repart vers le bas
        elif ligne == k - 1:
            direction = -1      # en bas -> on repart vers le haut

        ligne += direction      # on se déplace d'une ligne

    return indices


def rail_fence_chiffrer(texte: str, k: int) -> str:
    """Chiffre le texte avec la méthode Rail Fence à k niveaux."""
    if k <= 1 or k >= len(texte):
        return texte

    pattern = generer_pattern_indices(len(texte), k)

    # k rails = k listes de caractères
    rails: List[List[str]] = [[] for _ in range(k)]

    for ch, ligne in zip(texte, pattern):
        rails[ligne].append(ch)

    texte_chiffre = ""
    for rail in rails:
        texte_chiffre += "".join(rail)

    return texte_chiffre


def rail_fence_dechiffrer(texte_chiffre: str, k: int) -> str:
    """Déchiffre un texte chiffré avec la méthode Rail Fence à k niveaux."""
    if k <= 1 or k >= len(texte_chiffre):
        return texte_chiffre

    longueur = len(texte_chiffre)
    pattern = generer_pattern_indices(longueur, k)

    # Combien de lettres sur chaque ligne ?
    compte_par_ligne = [0] * k
    for ligne in pattern:
        compte_par_ligne[ligne] += 1

    # On découpe le texte chiffré en k morceaux (un par ligne)
    rails: List[List[str]] = []
    index = 0
    for count in compte_par_ligne:
        morceau = texte_chiffre[index : index + count]
        rails.append(list(morceau))
        index += count

    # On reconstruit le texte original en suivant le zigzag
    positions_actuelles = [0] * k
    resultat: List[str] = []

    for ligne in pattern:
        pos = positions_actuelles[ligne]
        resultat.append(rails[ligne][pos])
        positions_actuelles[ligne] += 1

    return "".join(resultat)


def afficher_zigzag(texte: str, k: int) -> None:
    """Affiche le texte sous forme de zigzag, pour visualiser les rails."""
    if k <= 1 or k >= len(texte):
        print("Zigzag non intéressant pour ce k (trop petit ou trop grand).")
        return

    pattern = generer_pattern_indices(len(texte), k)

    # On construit k lignes de texte, en mettant des espaces
    lignes: List[str] = []
    for num_ligne in range(k):
        ligne_texte = ""
        for i, ch in enumerate(texte):
            if pattern[i] == num_ligne:
                ligne_texte += ch
            else:
                ligne_texte += " "
        lignes.append(ligne_texte)

    print("\nReprésentation en zigzag :")
    for l in lignes:
        print(l)


def demander_entier_positif(message: str) -> int:
    """Redemande à l'utilisateur jusqu'à ce qu'il donne un entier > 0."""
    while True:
        valeur = input(message).strip()
        if valeur.isdigit() and int(valeur) > 0:
            return int(valeur)
        print("Veuillez entrer un entier strictement positif.")


def main() -> None:
    """Petit menu interactif pour montrer le chiffrement à ton professeur."""
    print("=== DEMO : Chiffrement Rail Fence à k niveaux ===")
    texte = input("Texte à traiter : ")

    k = demander_entier_positif("Nombre de niveaux (k) : ")

    mode = ""
    while mode not in {"c", "d"}:
        mode = input("Voulez-vous (c)hiffrer ou (d)échiffrer ? [c/d] : ").strip().lower()

    if mode == "c":
        resultat = rail_fence_chiffrer(texte, k)
        print("\nTexte chiffré :", resultat)
        afficher_zigzag(texte, k)
    else:
        resultat = rail_fence_dechiffrer(texte, k)
        print("\nTexte déchiffré :", resultat)
        afficher_zigzag(resultat, k)



if __name__ == "__main__":
    main()
