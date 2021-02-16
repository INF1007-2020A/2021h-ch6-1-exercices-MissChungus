#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        while len(values) < 10:
            values.append(input("Entrer une valeur: \n"))
        pass

    return sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words.append(input("Entrez le premier mot: \n"))
        words.append(input("Entrez le deuxième mot: \n"))

    return sorted(words[0]) == sorted(words[1])


def contains_doubles(items: list) -> bool:
    for element in items:
        if items.count(element) > 1:
            return True

    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    max = 0
    clé_max = None
    for clé in student_grades:
        somme = 0
        for value in student_grades[clé]:
            somme += value
            if somme/len(student_grades[clé]) > max:
                max = somme/len(student_grades[clé])
                clé_max = clé
    return {clé_max: max}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    frequency = {letter: sentence.count(letter) for letter in sentence}
    sorted_keys = sorted(frequency, reverse=True, key=frequency.__getitem__)
    for key in sorted_keys:
        if frequency[key] > 5:
            print(f"Le caractère {key} revient {frequency[key]} fois.")
    return frequency

def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    dict = {}
    clé = input("Veuillez entrer le nom de la recette : ")
    dict[clé] = input("Veuillez entrer les ingrédients de la recette sous forme de liste: ")
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    recherche = input("")
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
