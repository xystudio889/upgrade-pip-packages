from sys import argv
from os import system

system(f'python -m auto_upgrade_pip {' '.join(argv[1:])}')