#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")


def multiply_by_2(a_dictionary):
    new_dicti = {}
    for key, value in a_dictionary.items():
        new_dicti[key] = value * 2
    return new_dicti
