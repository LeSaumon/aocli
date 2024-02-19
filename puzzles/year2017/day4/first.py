from os.path import join
from rich import print as rprint

def solve():
	with open(join(__file__[:-8] + "data\input.txt"), "r") as file:
		result = 0
		data = [line.rstrip() for line in file]
		passphrases = [passphrase.split(" ") for passphrase in data]
		for phrase in passphrases:
			if len(set(phrase)) == len(phrase):
				result += 1
		rprint(result)
  
if '__name__' == '__main__':
	solve()