import os

FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'version.txt')

__version__ = None

if os.path.exists(FILE):
    with open(FILE, 'r', encoding='utf-8') as file:
        __version__ = file.read().split('\n')[0]
