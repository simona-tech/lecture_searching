from pathlib import Path
import json
import time
import generators as gen
import matplotlib.pyplot as plt


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
    with open(file_path, "r") as file:
        data = json.load(file)
        if field not in data:
            return None
        return data[field]

def main(file_path, field):
    sequential_data = read_data(file_path, field)
    print(sequential_data)
    return sequential_data

def linear_search(sequential_data, wanted_number):
    positions = []
    for idx, val in enumerate(sequential_data):
        if val == wanted_number:
            positions.append(idx)
    count = len(positions)
    return {"positions":positions,"count":count}

def binary_search(number_list, wanted_number):
    levy_okraj = 0
    pravy_okraj = len(number_list)-1
    while levy_okraj <= pravy_okraj:
        middle = (levy_okraj + pravy_okraj) // 2
        if number_list[middle] == wanted_number:
            return middle
        elif number_list[middle] < wanted_number:
            levy_okraj = middle +1
        elif number_list[middle] > wanted_number:
            pravy_okraj = middle -1
    return pravy_okraj

sizes = [100, 500, 1000, 5000, 10000]

linear_times = []
for n in sizes:
    lin_start = time.perf_counter()
    linear_search(gen.unordered_sequence(n),10)
    lin_end = time.perf_counter()
    duration = lin_end - lin_start
    linear_times.append(duration)

binary_times = []
for n in sizes:
    bin_start = time.perf_counter()
    binary_search(gen.unordered_sequence(n),10)
    bin_end = time.perf_counter()
    duration = bin_end - bin_start
    binary_times.append(duration)

plt.plot(sizes, binary_times)

plt.xlabel("Velikost vstupu")
plt.ylabel("Čas [s]")
plt.title("Ukázkový graf měření")
plt.show()

if __name__ == "__main__":
    print(linear_times)
    print(binary_times)
