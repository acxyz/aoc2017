import re



f = open('Day7input.txt','r')
message = f.read()
f.close()

lines = message.split("\n")

# okseah (78)
# ebmcu (30) -> glsrg, ckhip, rqhhyc, jjvxxtt, rdnpoms
# wuybunc (54)

# used named group:
rgx_line = re.compile(r"^(?P<name>\w+) \((?P<weight>\d+)\)( ->(?P<branches>( \w+\,?)+))?" )
rgx_branches = re.compile(r"\w+")

for line in lines:
	print(line)
	matches = rgx_line.match(line)
	if matches:
		# print ("match")
		# print(matches.group())
		# print (matches.groups())
		name = matches.group('name')
		weight = matches.group('weight')
		print (" - " + name + " [" + weight + "]")
		
		branches = matches.group('branches')
		if branches:
			
			l = rgx_branches.findall(branches)
			
			for branch in l: 
				print(" -- " + branch)
				
	else:
		print ("nomatch")
			

# for bank in banks: 
	# print(bank)

# def getMax (banks):
	# max_value = max(banks)
	# max_index = banks.index(max_value)
	# print (max_value)
	# print (max_index)
	# return (max_index, max_value)
	
# print("----------------------")

# print(banks)

# def redistributeMemory(banks):
	# (curr_index, num_to_distribute) = getMax(banks)
	# banks[curr_index] = 0
	# while num_to_distribute > 0:
		# curr_index += 1
		# if (curr_index) >= len(banks):
			# curr_index = 0
		# banks[curr_index] += 1
		# num_to_distribute -= 1


# iterations = 0

# states = set()
# statesDict = {} # phase 2
# states.add(tuple(banks))
# statesDict[tuple(banks)] = iterations


# while (True):
	# print ("Size is " + str(len(states)))
	# redistributeMemory(banks)
	# iterations += 1
	# print (banks)
	# if tuple(banks) in states:
		# break
	
	# states.add(tuple(banks))
	# statesDict[tuple(banks)] = iterations
	

# print (str(iterations) + " iterations")
# print (str(iterations - statesDict[tuple(banks)]) + " cycles since duple first appeared"	)
# # print (foo in states)
# # print(banks)
# # states.add(tuple(banks))
# # print ("Size is " + str(len(states)))
# # redistributeMemory(banks)
# # print(banks)
# # states.add(tuple(banks))
# # print ("Size is " + str(len(states)))
# # print (foo in states)
