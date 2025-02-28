# Meilleures pratiques de style de codage en Python
Ce projet est conçu pour améliorer la lisibilité et la maintenabilité du code en suivant les bonnes pratiques recommandées. 🐍✨

## 1. Respecter la PEP 8
- Utiliser des indentations de 4 espaces.
- Limiter la longueur des lignes à 79 caractères.
- Utiliser des noms de variables explicites et en minuscules avec des underscores (ex: `nom_utilisateur`).
- Séparer les classes et les fonctions avec deux lignes vides.
- **Référence** : [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

## 2. Utiliser des Docstrings et des commentaires
- Ajouter des docstrings pour les classes et les fonctions.
- Utiliser `#` pour des commentaires clairs et pertinents.
- **Référence** : [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)

## 3. Nommage des variables et fonctions (PEP 8 - Naming Conventions)
- Utiliser des noms explicites et descriptifs.
- Les variables et fonctions doivent être en `snake_case`.
- Les classes doivent être en `PascalCase`.
- Les constantes doivent être en `UPPER_CASE`. 
- **Référence** : [PEP 8 - Naming Conventions](https://peps.python.org/pep-0008/#naming-conventions)

## 4. Éviter les importations inutiles et privilégier des importations explicites
- Préférer `import module` plutôt que `from module import *`.
- Grouper les imports en trois catégories : standard, bibliothèques tierces, et modules internes.
```python
# 1. Importation des bibliothèques standard
import os
import sys

# 2. Importation des bibliothèques tierces
import numpy as np
import pandas as pd

# 3. Importation des modules locaux
from my_project.utils import helper_function
```
- **Référence** : [Python Import Best Practices](https://realpython.com/python-import/)

## 5. Utiliser des structures de contrôle claires
- Préférer les compréhensions de liste plutôt que les boucles `for` lorsque cela améliore la lisibilité.
- Éviter les conditions imbriquées complexes.

## 6. Gérer les exceptions correctement
- Utiliser `try-except` pour capturer les erreurs.
- Spécifier des exceptions précises plutôt que d'utiliser `except Exception:`.
- **Référence** : [Python Exception Handling](https://realpython.com/python-exceptions/)

## 7. Utiliser des types et annotations
- Ajouter des annotations de type pour améliorer la lisibilité et la détection d'erreurs (`def addition(a: int, b: int) -> int:`).
- **Référence** : [PEP 484 – Type Hints](https://peps.python.org/pep-0484/)

## 8. Optimiser la lisibilité du code
- Découper les fonctions longues en plusieurs petites fonctions claires.
- Suivre le principe DRY (Don't Repeat Yourself).
- **Référence** : [Don’t repeat yourself: Python functions](https://scientificallysound.org/2018/07/19/python-functions/)

## 9. Adopter un formatage automatique
- Utiliser des outils comme `black`, `flake8`, ou `isort` pour standardiser le style.
- **Référence** : [Black – The Uncompromising Code Formatter](https://black.readthedocs.io/en/stable/)

## 10. Utiliser des environnements virtuels
- Travailler avec `venv` ou `conda` pour gérer les dépendances.
- **Référence** : [Python Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)

## 11. Écrire des tests unitaires
- Utiliser `pytest` ou `unittest` pour garantir la fiabilité du code.
- Rédiger des tests couvrant les cas critiques et limites.
- **Référence** : [Python Unit Testing](https://realpython.com/python-testing/)
