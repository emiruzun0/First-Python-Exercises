with open ("spider.txt") as file:
	for line in file:
		print(line.upper())

with open("spider.txt") as file:   #Avoid getting the empty lines
	for line in file:
		print(line.strip().upper())  #Strip removes all surrounding white space

file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)