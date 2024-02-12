from os.path import join
from rich import print as rprint

def solve():
	with open(join(__file__[:-8] + "data\input.txt"), "r") as file:
		data = file.readline().replace("\n", "")

if '__name__' == '__main__':
	solve()