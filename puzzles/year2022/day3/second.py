import string
from rich import print as rprint
from os.path import join


def solve():
	with open(join(__file__[:-9] + "data\input.txt")) as file:
		bags = file.read().splitlines()
		alphabet = string.ascii_letters
		points = {}

		# Build the data structure
		pre_groups = [bags[i:i+3] for i in range(0, len(bags), 3)]

		# Process strings in sets to compare with set.intersection()
		post_process_groups = [[set(string) for string in group] for group in pre_groups]

		# Build the points mapper
		for value, character in enumerate(alphabet, 1):
			points[character] = value

		answers = []
		# Compare bags and add the value of the badge to the answer
		for group in post_process_groups:
			result = set.intersection(*group)
			answers.append(points[next(iter(result))])
		rprint(sum(answers))

if '__name__' == '__main__':
	solve()