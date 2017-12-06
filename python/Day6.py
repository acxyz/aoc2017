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

redistributeMemory(banks)
print(banks)

redistributeMemory(banks)
print(banks)
		
