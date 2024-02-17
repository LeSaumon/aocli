from os.path import join
from rich import print as rprint

def solve():
	with open(join(__file__[:-9] + "data\input.txt"), "r") as file:
		data = file.readline().replace("\n", "")
		half = len(data) / 2
		splitted_data_a = list(enumerate(data[:int(half)]))
		splitted_data_b = list(enumerate(data[int(half):]))
		result = 0
		for index, val in splitted_data_a:
			if int(val) == int(splitted_data_b[index][1]):
				result += int(val) * 2
		rprint(result)


if '__name__' == '__main__':
	solve()