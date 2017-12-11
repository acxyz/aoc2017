import sys


def inititalizeList(length):
	list = []
	for i in range (length):
		list.append(i)
	return list


def getList(list, curr_pos, size):
	# print(list)
	rev_list = []
	cp = curr_pos
	for i in range(size):
		if (cp > len(list) -1):
			cp -= len(list)
		rev_list.append(list[cp])
		cp += 1
	# print (rev_list)
	return rev_list
	
def putList(list, curr_pos, repl_list):
	out_list = list
	cp = curr_pos
	for i in range( len(repl_list) ):
		if (cp > len(list) -1):
			cp -= len(list)
		out_list[cp] = repl_list[i]
		cp+=1
	return out_list
	
def reverse(list, curr_pos, size):
	rev_list = getList(list, curr_pos, size)
	# if GLB_DEBUG:
		# print(rev_list)
	rev_list.reverse()
	# if GLB_DEBUG:
		# print(rev_list)
	list = putList(list, curr_pos, rev_list)
	# if GLB_DEBUG:
		# print (list)
	return list
	
def getTransformedList(the_list, input_sequence, current_position, skip_size):
	# list = inititalizeList(list_length)
	if GLB_DEBUG:
		print ("")
		print ("*******************************")
		print ("")
		print ("Initital List: " + str(the_list))

	# for i in list:
		# print(i)

	for i in input_sequence:
		if GLB_DEBUG:
			print ("")
			print(i)
			print (str(skip_size) + " is skip size")
		# print(the_list)
		
		the_list = reverse(the_list, current_position, i)
		
		# if GLB_DEBUG:
			# print(the_list)
		
		j = i + current_position + skip_size
		
		while j > len(the_list) - 1:
			j -= len(the_list)
		
		current_position = j
		skip_size += 1
		if skip_size == len(the_list):
			skip_size = 0
		
		if GLB_DEBUG:
			print (str(current_position) + " is curr pos")
			print ("--------------------------------------------------")
			# input("Press key to continue")
	return (the_list, current_position, skip_size)

	
print("")

print("-----------------------------------------")

GLB_DEBUG = False

list_length = 5
input_sequence = [3, 4, 1, 5]
(lyst, cp, ss) = getTransformedList(inititalizeList(list_length), input_sequence, 0, 0)
	
print("Check: " + str( lyst[0] * lyst[1])	)

if (lyst[0] * lyst[1] != 12):
	print ("Test failed on getTransformedList")
	sys.exit(0)
else:
	print("get transformed list success")

print("-----------------------------------------")







list_length = 256
input_sequence = [227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144]
(lyst, cp, ss) = getTransformedList(inititalizeList(list_length), input_sequence, 0, 0)
print("check: " + str( lyst[0] * lyst[1])	)

if (lyst[0] * lyst[1] != 13760):
	print ("Test failed on getTransformedList")
	sys.exit(0)
else:
	print("get transformed list success")


print("-----------------------------------------")

# sys.exit()




def asciify(str):
	# for code in str.encode('ascii'):
		# print(code)
	return list(str.encode('ascii')) + [17, 31, 73, 47, 23]

def densify(list):
	if GLB_DEBUG:
		print(list)
	total = 0
	start = 0
	result_list = []
	while start < len(list):
		result = 0
		for i in range (16):
			if start + i < len(list):
				result ^= list[start + i]
				# print(list[start+i])
				# print(result)
		result_list.append(result)
		# print(result_list)
		start += 16
	return result_list
	
def hexify(list):
	result = ""
	for x in list:
		# result += hex(x)[2:4]
		hexx = format(x,'x')
		if len(hexx) == 1:
			hexx = '0' + hexx
		result += hexx
	return result

	
def sparseHashify(input_string):
	if GLB_DEBUG:
		print("")
		print("")
		print ("Input string is " +  input_string)
	
	list_length = 256
	my_list = inititalizeList(list_length)
	
	input_sequence = asciify(input_string)

	if GLB_DEBUG:
		print("input seq is " + str(input_sequence))

	cp = 0
	ss = 0

	for i in range (64):
		if GLB_DEBUG:
			print("")
			print ("***** I is " + str(i) + "*******")
			print ("CP/SS: " + str(cp) + "/" + str(ss))
		(my_list, cp, ss) = getTransformedList(my_list, input_sequence, cp, ss)
	
	return(my_list)
		


def hexifyString(input_string):

	my_list = sparseHashify(input_string)
	if GLB_DEBUG:
		print ("Sparse Hash " + str(my_list))
	dense_hash = densify(my_list)
	if GLB_DEBUG:
		print (dense_hash)
	hex_string = hexify(dense_hash)
	if GLB_DEBUG:
		print (hex_string)
	return hex_string
	

test_list = [64, 7, 255]
result_string = hexify(test_list)
print("Hexify: " + result_string)
if result_string != '4007ff':
	print ("Error in hexify function")
	sys.exit()
	
	
test_list = [65 , 27 , 9 , 1 , 4 , 3 , 40 , 50 , 91 , 7 , 6 , 0 , 2 , 5 , 68 , 22]	
test_result = densify(test_list)
if test_result != [64]:
	print ("Error in densify function")
	sys.exit()			
else:
	print("Densify: " + str(test_result))
	
input_string = "1,2,3"
test_result = asciify(input_string)
if test_result != [49,44,50,44,51,17,31,73,47,23]:
	print ("Error in asciify function")
	sys.exit()
else:
	print(test_result)	


GLB_DEBUG = False

if (sparseHashify("AoC 2017") != [2,43,207,224,132,199,217,27,176,138,9,177,228,225,153,170,140,244,240,1,7,230,142,114,148,229,60,28,163,3,48,186,24,166,174,106,34,152,20,95,187,59,61,155,179,220,47,6,84,83,188,87,68,154,226,233,42,137,189,194,168,160,109,180,38,117,251,151,162,123,192,98,214,72,127,10,56,121,122,126,202,79,245,175,216,112,136,91,0,8,55,94,46,193,238,85,135,104,82,110,144,70,29,156,105,143,5,211,147,37,215,69,201,52,172,253,128,158,64,4,221,67,18,248,107,39,167,66,213,157,146,171,111,36,125,93,219,169,239,205,197,50,78,65,13,124,133,89,116,99,118,62,75,96,63,231,131,53,184,250,101,185,249,210,73,212,145,74,11,71,190,130,139,183,191,222,86,21,150,247,40,26,45,77,19,149,23,237,254,100,227,236,173,161,102,141,235,76,33,252,255,115,206,218,243,232,242,204,80,103,203,88,14,51,209,134,223,200,30,165,195,129,208,58,196,92,178,90,54,41,108,113,49,15,16,57,198,12,31,22,159,97,81,234,181,241,182,35,246,120,44,119,25,17,32,164]):
	print ("Error in sparse hash AoC 2017")
	sys.exit(0)
else:
	print ("Sparse hash successful")


if (sparseHashify("") != [38,171,116,63,70,137,168,29,198,55,160,15,34,95,58,7,188,189,238,141,30,31,124,241,20,1,244,203,234,73,236,211,122,197,94,227,142,57,72,239,54,81,154,217,10,13,186,161,6,17,128,105,106,69,44,51,248,23,136,173,52,39,40,5,254,195,64,187,192,37,230,153,56,177,84,147,96,249,252,121,166,143,62,169,90,99,196,155,132,159,162,229,76,117,164,127,150,21,88,27,242,67,114,115,226,191,190,53,2,65,206,205,24,251,14,75,74,247,80,11,50,181,46,101,100,179,48,131,32,97,102,201,170,93,104,103,182,125,12,43,220,113,158,167,68,47,66,33,112,135,194,185,218,219,8,245,130,253,204,243,202,109,92,209,156,133,250,107,4,183,60,215,172,231,240,83,98,193,82,139,210,91,146,85,184,163,140,145,178,35,232,151,214,213,200,199,18,221,212,9,152,123,78,3,228,25,26,225,0,61,138,255,222,233,110,129,208,207,176,235,108,77,148,19,180,79,28,149,224,237,86,157,216,111,22,89,16,41,144,71,134,59,246,165,174,223,118,119,36,175,126,87,120,45,42,49]):
	print ("Error in sparse hash")
	sys.exit(0)
else:
	print ("Sparse hash successful")	

print("-----------------------------------------")

print("-----------------------------------------")
	
# sys.exit()	

GLB_DEBUG = False

# The empty string becomes a2582a3a0e66e6e86e3812dcb672a272.
# AoC 2017 becomes 33efeb34ea91902bb2f59c9920caa6cd.
# 1,2,3 becomes 3efbe78a8d82f29979031a4aa0b16a9d.
# 1,2,4 becomes 63960835bcdc130f0b66d7ff4f6a5a8e.

foo1 = hexifyString("")
foo2 = hexifyString("AoC 2017")
foo3 = hexifyString("1,2,3")
foo4 = hexifyString("1,2,4")

if foo1 != "a2582a3a0e66e6e86e3812dcb672a272":
	print ("HexifyString failed for empty string")
	sys.exit()
else:
	print ("Empty String: " + foo1)
	
if foo2 != "33efeb34ea91902bb2f59c9920caa6cd":
	print ("HexifyString failed for AoC 2017")
	sys.exit()
else:
	print ("AoC 2017: " + foo2)

if foo3 != "3efbe78a8d82f29979031a4aa0b16a9d":
	print ("HexifyString failed for 1,2,3")
	sys.exit()
else:
	print ("1,2,3: " + foo1)

if foo4 != "63960835bcdc130f0b66d7ff4f6a5a8e":
	print ("HexifyString failed for 1,2,4")
	sys.exit()
else:
	print ("1,2,4: " + foo1)	

print("")
print(" * * * ALL TESTS PASS!! * * * ")
print("")

# --- Day 10: Knot Hash ---

# You come across some programs that are trying to implement a software emulation of a hash based on knot-tying. The hash these programs are implementing isn't very strong, but you decide to help them anyway. You make a mental note to remind the Elves later not to invent their own cryptographic functions.

# This hash function simulates tying a knot in a circle of string with 256 marks on it. Based on the input to be hashed, the function repeatedly selects a span of string, brings the ends together, and gives the span a half-twist to reverse the order of the marks within it. After doing this many times, the order of the marks is used to build the resulting hash.

  # 4--5   pinch   4  5           4   1
 # /    \  5,0,1  / \/ \  twist  / \ / \
# 3      0  -->  3      0  -->  3   X   0
 # \    /         \ /\ /         \ / \ /
  # 2--1           2  1           2   5
# To achieve this, begin with a list of numbers from 0 to 255, a current position which begins at 0 (the first element in the list), a skip size (which starts at 0), and a sequence of lengths (your puzzle input). Then, for each length:

# Reverse the order of that length of elements in the list, starting with the element at the current position.
# Move the current position forward by that length plus the skip size.
# Increase the skip size by one.
# The list is circular; if the current position and the length try to reverse elements beyond the end of the list, the operation reverses using as many extra elements as it needs from the front of the list. If the current position moves past the end of the list, it wraps around to the front. Lengths larger than the size of the list are invalid.

# Here's an example using a smaller list:

# Suppose we instead only had a circular list containing five elements, 0, 1, 2, 3, 4, and were given input lengths of 3, 4, 1, 5.

# The list begins as [0] 1 2 3 4 (where square brackets indicate the current position).
# The first length, 3, selects ([0] 1 2) 3 4 (where parentheses indicate the sublist to be reversed).
# After reversing that section (0 1 2 into 2 1 0), we get ([2] 1 0) 3 4.
# Then, the current position moves forward by the length, 3, plus the skip size, 0: 2 1 0 [3] 4. Finally, the skip size increases to 1.
# The second length, 4, selects a section which wraps: 2 1) 0 ([3] 4.
# The sublist 3 4 2 1 is reversed to form 1 2 4 3: 4 3) 0 ([1] 2.
# The current position moves forward by the length plus the skip size, a total of 5, causing it not to move because it wraps around: 4 3 0 [1] 2. The skip size increases to 2.
# The third length, 1, selects a sublist of a single element, and so reversing it has no effect.
# The current position moves forward by the length (1) plus the skip size (2): 4 [3] 0 1 2. The skip size increases to 3.
# The fourth length, 5, selects every element starting with the second: 4) ([3] 0 1 2. Reversing this sublist (3 0 1 2 4 into 4 2 1 0 3) produces: 3) ([4] 2 1 0.
# Finally, the current position moves forward by 8: 3 4 2 1 [0]. The skip size increases to 4.
# In this example, the first two numbers in the list end up being 3 and 4; to check the process, you can multiply them together to produce 12.

# However, you should instead use the standard list size of 256 (with values 0 to 255) and the sequence of lengths in your puzzle input. Once this process is complete, what is the result of multiplying the first two numbers in the list?

# Your puzzle answer was 13760.

# The first half of this puzzle is complete! It provides one gold star: *

# --- Part Two ---

# The logic you've constructed forms a single round of the Knot Hash algorithm; running the full thing requires many of these rounds. Some input and output processing is also required.

# First, from now on, your input should be taken not as a list of numbers, but as a string of bytes instead. Unless otherwise specified, convert characters to bytes using their ASCII codes. This will allow you to handle arbitrary ASCII strings, and it also ensures that your input lengths are never larger than 255. For example, if you are given 1,2,3, you should convert it to the ASCII codes for each character: 49,44,50,44,51.

# Once you have determined the sequence of lengths to use, add the following lengths to the end of the sequence: 17, 31, 73, 47, 23. For example, if you are given 1,2,3, your final sequence of lengths should be 49,44,50,44,51,17,31,73,47,23 (the ASCII codes from the input string combined with the standard length suffix values).

# Second, instead of merely running one round like you did above, run a total of 64 rounds, using the same length sequence in each round. The current position and skip size should be preserved between rounds. For example, if the previous example was your first round, you would start your second round with the same length sequence (3, 4, 1, 5, 17, 31, 73, 47, 23, now assuming they came from ASCII codes and include the suffix), but start with the previous round's current position (4) and skip size (4).

# Once the rounds are complete, you will be left with the numbers from 0 to 255 in some order, called the sparse hash. Your next task is to reduce these to a list of only 16 numbers called the dense hash. To do this, use numeric bitwise XOR to combine each consecutive block of 16 numbers in the sparse hash (there are 16 such blocks in a list of 256 numbers). So, the first element in the dense hash is the first sixteen elements of the sparse hash XOR'd together, the second element in the dense hash is the second sixteen elements of the sparse hash XOR'd together, etc.

# For example, if the first sixteen elements of your sparse hash are as shown below, and the XOR operator is ^, you would calculate the first output number like this:

# 65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22 = 64
# Perform this operation on each of the sixteen blocks of sixteen numbers in your sparse hash to determine the sixteen numbers in your dense hash.

# Finally, the standard way to represent a Knot Hash is as a single hexadecimal string; the final output is the dense hash in hexadecimal notation. Because each number in your dense hash will be between 0 and 255 (inclusive), always represent each number as two hexadecimal digits (including a leading zero as necessary). So, if your first three numbers are 64, 7, 255, they correspond to the hexadecimal numbers 40, 07, ff, and so the first six characters of the hash would be 4007ff. Because every Knot Hash is sixteen such numbers, the hexadecimal representation is always 32 hexadecimal digits (0-f) long.

# Here are some example hashes:

# The empty string becomes a2582a3a0e66e6e86e3812dcb672a272.
# AoC 2017 becomes 33efeb34ea91902bb2f59c9920caa6cd.
# 1,2,3 becomes 3efbe78a8d82f29979031a4aa0b16a9d.
# 1,2,4 becomes 63960835bcdc130f0b66d7ff4f6a5a8e.
# Treating your puzzle input as a string of ASCII characters, what is the Knot Hash of your puzzle input? Ignore any leading or trailing whitespace you might encounter.