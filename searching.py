from dataclasses import field
from itertools import count
from pathlib import Path
import json

from generators import ordered_sequence


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

    with open("sequential.json", "r") as file:
        data = json.load(file)
    return data[field]

def linear_search(sequence, number):
    count = 0
    position = []
    no_count = 0
    for i,num in enumerate(sequence):
        if number == num:
            count += 1
            position.append(i)
        else:
            no_count += 1

    if no_count < len(sequence):
        return {
        'positions': position,
        'count': count
    }
    else:
        return None

def binary_search(sequence, number):
    mid = (max + min)/2

def main():
    sequen_data = read_data("sequential.json", 'unordered_numbers')
    print(sequen_data)

    number = 0
    linear = linear_search(sequen_data, number)
    print(linear)


    if field() == 'unordered_numbers' or field() == 'ordered_numbers':
        return list
    elif field() == 'dna_sequence':
        return str
    else:
        return None



if __name__ == "__main__":
    main()
