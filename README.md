# Firefox Control Script

Script Python pour contrôler Firefox à distance sur macOS en envoyant des événements clavier directement au processus.

## Fonctionnalités

- Envoie des touches clavier à Firefox sans avoir besoin de le focus
- Séquence automatisée avec délais aléatoires
- Contrôle depuis un terminal pendant que vous utilisez d'autres applications

## Prérequis

- macOS
- Python 3
- Firefox

## Installation

1. Cloner le repository:
```bash
git clone https://github.com/cyphalle/firefox-control.git
cd firefox-control
```

2. Créer l'environnement virtuel et installer les dépendances:
```bash
python3 -m venv firefox_control_env
source firefox_control_env/bin/activate
pip install pyobjc-framework-Quartz
```

## Utilisation

Lancer le script avec:
```bash
./run_firefox_control.sh
```

Ou directement:
```bash
firefox_control_env/bin/python3 control_firefox.py
```

Pour arrêter le script, appuyez sur `Ctrl+C`.

## Séquence

Le script répète la séquence suivante en boucle:

1. Attente aléatoire (1-5 secondes)
2. PAGE_DOWN 1×
3. Attente aléatoire (1-3 secondes)
4. PAGE_DOWN 2×
5. Attente aléatoire (1-5 secondes)
6. PAGE_DOWN 2×
7. Attente aléatoire (1-5 secondes)
8. Flèche droite →
9. Recommence

## Personnalisation

Modifiez le fichier `control_firefox.py` pour:
- Changer les délais aléatoires
- Modifier le nombre de PAGE_DOWN
- Ajouter d'autres touches (keycodes disponibles dans le script)

## Keycodes disponibles

```python
RIGHT = 124
DOWN = 125
LEFT = 123
UP = 126
ENTER = 36
SPACE = 49
PAGE_DOWN = 121
```

## Licence

MIT
