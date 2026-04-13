from pathlib import Path
import json


def read_data(file_name, field):
    """
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
    with open(file_name, "r") as file:
        data = json.load(file)
        if field not in data:
            return None
        return data[field]

def main(file_name, field):
    sequential_data = read_data(file_name, field)
    print(sequential_data)
    return None


if __name__ == "__main__":
    main("sequential.json", "unordered_numbers")
