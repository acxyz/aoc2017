def cleanStream(stream):
	
	result = ""
	readingGarbage = False
	i = -1
	lgth = len(stream)
	
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
		else:
			if thisChar == '!':
				i += 1;
			elif thisChar == '>':
				readingGarbage = False;
			
		
		

	return result
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

