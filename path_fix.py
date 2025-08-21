import sys, os

MODULES_PATH = os.path.join(os.path.dirname(__file__), 'Modules')

if MODULES_PATH not in sys.path:
    sys.path.append(MODULES_PATH)
