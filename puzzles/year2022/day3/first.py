from rich import print as rprint
from os.path import join

def solve():
	with open(join(__file__[:-8] + "data\input.txt"), "r") as file:
		bags = file.read().splitlines()

		alphabet = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()
		points = {}
		answer = []
		# Build the points mapper
		for value, character in enumerate(alphabet, 1):
			points[character] = value

		for bag in bags:
			bag_size = len(bag)
			container_size = len(bag) // 2
			container_1 = bag[0:container_size]
			container_2 = bag[container_size:bag_size]
			# Add to list the item value IF an item is found in both container
			answer.append(list(set([points[container_2[container_2.find(item)]] for item in container_1 if container_2.find(item) != -1])))
		rprint(sum([sum(result) for result in answer]))

if '__name__' == '__main__':
	solve()