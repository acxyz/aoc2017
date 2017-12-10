import sys

def cleanStream(stream):
	
	result = ""
	readingGarbage = False
	i = -1
	lgth = len(stream)
	
	depth = 1
	score = 0
	
	garbageChar = 0
	
	# print(str(lgth) + " is length" )
	while i < lgth - 1:
		i += 1
		# print ("i is " + str(i))
		thisChar = stream[i]
		if not readingGarbage:
			if thisChar == '<':
				readingGarbage = True
			else:
				result += thisChar;
				if thisChar == '{':
					depth += 1
				elif thisChar == '}':
					depth -= 1
					score += depth
		else:
			if thisChar == '!':
				i += 1;
			
			elif thisChar == '>':
				readingGarbage = False;
			else:
				garbageChar += 1
				
			
		
		

	return (result, score, garbageChar)
####

	
test1= "{}"
test2 = "{{{}}}" # score of 1 + 2 + 3 = 6.
test3 = "{{},{}}" # score of 1 + 2 + 2 = 5.
test4 = "{{{},{},{{}}}}" # score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
test5 = "{<a>,<a>,<a>,<a>}" #, score of 1.
test6 = "{{<ab>},{<ab>},{<ab>},{<ab>}}" #, score of 1 + 2 + 2 + 2 + 2 = 9.
test7 = "{{<!!>},{<!!>},{<!!>},{<!!>}}" #, score of 1 + 2 + 2 + 2 + 2 = 9.
test8 = "{{<a!>},{<a!>},{<a!>},{<ab>}}" #, score of 1 + 2 = 3.

print (cleanStream(test1)) 
print (cleanStream(test2)) 
print (cleanStream(test3)) 
print (cleanStream(test4)) 
print (cleanStream(test5)) 
print (cleanStream(test6)) 
print (cleanStream(test7)) 
print (cleanStream(test8)) 

if len(sys.argv) > 1:
	inputFile = sys.argv[1]
	fileToRead = open(inputFile,'r')
	inputStream = fileToRead.read()
	fileToRead.close()
	
	output = cleanStream(inputStream)
	
	print ("Value of Input Stream is " + str(output[1]))
	print ("Number of garbage is "+ str(output[2]))
