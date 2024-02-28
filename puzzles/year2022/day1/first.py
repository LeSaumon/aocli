from rich import print as rprint
from os.path import join

def solve():
	with open(join(__file__[:-8] + "data\input.txt"), "r") as file:
		result = {}
		file_length = len(file.readlines()) - 1
		file.seek(0)
		elf = 0
		for count, line in enumerate(file):
			# Instantiate the data related to a single elf
			if f"Elf-{elf}" not in result:
				result[f"Elf-{elf}"] = {
					"values": []
				}
			# To split values between each elves
			if line == "\n" or count == file_length:
				result[f"Elf-{elf}"]["sum"] = sum(result[f"Elf-{elf}"]["values"])
				elf += 1

			else:
				result[f"Elf-{elf}"]["values"].append(int(line))

		calories = max(elf["sum"] for elf in result.values())
		rprint(calories)

if '__name__' == '__main__':
	solve()