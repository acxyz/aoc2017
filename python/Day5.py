f = open('Day5Maze.txt','r')
message = f.read()

f.close()

lines = list(map(int ,message.split("\n")))

# print(len(lines))
# print (lines[0])
# print (lines[1073])

min_i = 0
max_i = len(lines) -1
# print (min_i)
# print (max_i)

# for i in range (0, max_i):
	# lines[i] = int(lines[i])

i = 0
counter = 0
while (i >= min_i and i <= max_i):

	this_val = lines[i]
	print (str(i) + ": " + str(this_val))
	lines[i] += -1 if this_val >= 3 else 1
	counter +=  1
	i += this_val
	# input ("press enter to continue")
	
	
print ("final value: " + str(counter))