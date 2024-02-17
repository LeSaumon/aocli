from re import findall
from os.path import join
from rich import print as rprint

def check( data):
	for val in data:
		if res := list(filter(lambda x: val % x == 0 and val != x , data)):
			return (res[0], val)

def solve():
	with open(join(__file__[:-9] + "data\input.txt"), "r") as file:
		result = 0
		for line in file.readlines():
			line_data = [int(x) for x in findall(r"\d+", line)]
			values = check(line_data)
			result += values[1] // values[0]
		rprint(result)

if '__name__' == '__main__':
	solve()