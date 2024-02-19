from os.path import join
from rich import print as rprint

def solve():
	with open(join(__file__[:-9] + "data\input.txt"), "r") as file:
		result = 0
		sorted_data = []
		unsorted_data = [passphrase.split(" ") for passphrase in [line.rstrip() for line in file]]
		for passphrase in unsorted_data:
			sorted_data.append([''.join(sorted(word)) for word in passphrase])
		for phrase in sorted_data:
			if len(set(phrase)) == len(phrase):
				result += 1
		rprint(result)

if '__name__' == '__main__':
	solve()