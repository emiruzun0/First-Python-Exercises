file = open("spider.txt")
print(file.readline())  #Read a line
print(file.readline())

print(file.read()) #Read from wherever currently are until the file ends

file.close()


with open ("spider.txt") as file:  #Python will automatically close the file
	print(file.readline())