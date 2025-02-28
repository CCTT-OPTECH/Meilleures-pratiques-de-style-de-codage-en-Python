"""
Exemple illustrant les conventions de nommage selon PEP 8 en Python.
Utiliser des espaces autour des opérateurs et après les virgules.
"""
# 1. Importation des bibliothèques standard
import os
import sys

# 2. Importation des bibliothèques tierces
import numpy as np
import pandas as pd

# 3. Importation des modules locaux
#from my_project.utils import helper_function
#from my_project.models import CustomModel

# Évitez les importations génériques comme :
# from module import *
# car elles polluent l'espace de noms et rendent le code difficile à comprendre.

# Déclaration d'une constante en UPPER_CASE
MAX_USERS = 100

# Déclaration d'une variable en snake_case
submitted = 0
submitted += 1

# List
my_list = [1, 2, 3, 4, 5, 6]

# Opération
submitted = MAX_USERS + 1


# Définition d'une fonction en snake_case
def create_default_user():
    """Crée et retourne un utilisateur par défaut."""
    return "John Doe", 30


# Définition d'une classe en PascalCase
class Person:
    """Classe représentant une personne avec un nom et un âge."""

    def __init__(self, name: str, age: int):
        """Initialise une personne avec un nom et un âge."""
        self.name = name  # Variable d'instance en snake_case
        self.age = age

    def introduce(self) -> str:
        """Retourne une présentation de la personne."""
        return f"Bonjour, je m'appelle {self.name} et j'ai {self.age} ans."


# Utilisation des conventions de nommage
if __name__ == "__main__":
    default_user = Person("John Doe", 30)
    print(default_user.introduce())
