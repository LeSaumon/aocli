from rich import print as rprint
from os.path import join

def solve():
	with open(join(__file__[:-8] + "data\input.txt"), "r") as file:
		data = file.readline().replace("\n", "")
		result = 0
		for i, char in enumerate(data):
			try:
				next = data[i + 1]
			except IndexError:
				next = data[0]
			if char == next:
				result += int(char)
		rprint(result)

if '__name__' == '__main__':
	solve()