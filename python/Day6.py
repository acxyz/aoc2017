# from sets import Set

source = "0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11"
# test dupe:
# source = "0	5	14	0	11	14	13	4	11	8	8	7	1	4	12	11"

banks = list(map(int, source.split("\t")))

for bank in banks: 
	print(bank)

def getMax (banks):
	max_value = max(banks)
	max_index = banks.index(max_value)
	print (max_value)
	print (max_index)
	return (max_index, max_value)
	
print("----------------------")

print(banks)

def redistributeMemory(banks):
	(curr_index, num_to_distribute) = getMax(banks)
	banks[curr_index] = 0
	while num_to_distribute > 0:
		curr_index += 1
		if (curr_index) >= len(banks):
			curr_index = 0
		banks[curr_index] += 1
		num_to_distribute -= 1

states = set()
states.add(tuple(banks))
foo = tuple(banks)

iterations = 0

while (True):
	print ("Size is " + str(len(states)))
	redistributeMemory(banks)
	iterations += 1
	print (banks)
	if tuple(banks) in states:
		break
	
	states.add(tuple(banks))
	

print (str(iterations) + " iterations")
	
# print (foo in states)
# print(banks)
# states.add(tuple(banks))
# print ("Size is " + str(len(states)))
# redistributeMemory(banks)
# print(banks)
# states.add(tuple(banks))
# print ("Size is " + str(len(states)))
# print (foo in states)
