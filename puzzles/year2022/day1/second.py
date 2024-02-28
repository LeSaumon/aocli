from rich import print as rprint
from os.path import join

def solve():
	with open(join(__file__[:-9] + "data\input.txt"), "r") as file:
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

		# Build a list with all the sums of the elves
		elves_calories_sums = [value['sum'] for value in result.values()]
		top_3_elves_sums = []

		# Iterate over elves_calories_sums to extract the 3 maximum values
		for _ in range(3):
			max_value = max(elves_calories_sums)
			top_3_elves_sums.append(max_value)
			# Delete the max_value to not get it the next iteration
			elves_calories_sums.pop(elves_calories_sums.index(max_value))

		rprint(sum(top_3_elves_sums))
if '__name__' == '__main__':
	solve()