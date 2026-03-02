#!/usr/bin/python3
"""
This module provides a function to convert CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it to a JSON file (data.json).
    Returns True if successful, False if the file is not found.
    """
    try:
        data = []
        with open(csv_filename, encoding='utf-8') as csv_f:
            # CSV sətirlərini lüğətə çeviririk
            reader = csv.DictReader(csv_f)
            for row in reader:
                data.append(row)

        with open('data.json', 'w', encoding='utf-8') as json_f:
            # Siyahını JSON faylına yazırıq
            json.dump(data, json_f)

        return True
    except FileNotFoundError:
        return False
