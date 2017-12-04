

f = open('Day4PassPhrases.txt','r')
message = f.read()

f.close()

lines = message.split("\n");

i = 0
for line in lines:
	if len(line) == 0:
		next
		
	# print(str(i))
	lineIsGood = True;
	
	
	words = line.split()
	
	wordCount = dict()
	if (len(words)== 0):
		lineIsGood = False
	else :
		for word in words:
			# print(word)
			
			if word in wordCount:
				lineIsGood = False;
				# print (line)
				break;
			else:
				
				wordCount[word] = 1;
	
	
	if lineIsGood:
		# print ("'" + line + "'")
		i += 1;

		
print (str(i) + " valid passphrases")
