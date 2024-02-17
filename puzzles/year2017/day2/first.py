from re import findall
from os.path import join
from rich import print as rprint

def solve():
	with open(join(__file__[:-8] + "data\input.txt"), "r") as file:
		result = 0
		for line in file.readlines():
			# parse data to retrieve lowest and highest values
			values = sorted([int(x) for x in findall(r"\d+", line)])
			result += values[-1] - values[0]
		rprint(result)

if '__name__' == '__main__':
	solve()