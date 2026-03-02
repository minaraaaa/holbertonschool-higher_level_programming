#!/usr/bin/python3
"""
This module provides functionality to serialize a dictionary to XML
and deserialize XML back to a dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Reads an XML file and returns a deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # XML elementlərini lüğətə yığırıq
        return {child.tag: child.text for child in root}
    except FileNotFoundError:
        return None
