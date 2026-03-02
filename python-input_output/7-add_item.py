#!/usr/bin/python3
"""
Adds all arguments to a Python list, and then save them to a file.
"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Əgər fayl varsa, içini oxuyuruq, yoxdursa boş siyahı yaradırıq
try:
    items = load_from_json_file(filename)
except (FileNotFoundError, ValueError):
    items = []

# Terminaldan gələn arqumentləri (skriptin adından sonrakıları) siyahıya əlavə edirik
items.extend(sys.argv[1:])

# Siyahını yenidən fayla yazırıq
save_to_json_file(items, filename)
