import os
import sys

# Ajouter le répertoire courant au path
sys.path.insert(0, os.path.abspath("."))

# Importer l'application
from bezier_editor.app import main

# Exécuter l'application
if __name__ == "__main__":
    main()