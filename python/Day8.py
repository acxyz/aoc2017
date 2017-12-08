import re
import sys

testArray = [
"b inc 5 if a > 1",
"a inc 1 if b < 5",
"c dec -10 if a >= 1",
"c inc -20 if c == 10",
]

# rgx_line = re.compile(r"^(?P<name>\w+) (?P<operator>\w\w\w) (?P<amount>-?\d+) (?P<condition>if .+)" )
rgx_line = re.compile(r"^(?P<operation>(?P<name1>\w+) \w\w\w -?\d+) (?P<condition>if (?P<name2>\w+) .+)" )




def processRegisterInstructions(lines):
	registers = {}
	registers["highestValue"] = 0
	
	for line in lines:
		print(line)

		matches = rgx_line.match(line)
		if matches:
		
			name1 = matches.group('name1')
			name2 = matches.group('name2')
			# print(name1)
			# print(name2)
			
			try: 
				exec(name1)
			except NameError:
				exec(name1 + " = 0")
				
			try: 
				exec(name2)
			except NameError:
				exec(name2 + " = 0")

			# operator = matches.group('operator')
			# amount = matches.group('amount')
			operation = matches.group("operation")
			condition = matches.group('condition')
			
			
			operation = operation.replace("inc","+=")
			operation = operation.replace("dec","-=")
			
			command = condition + ": \t" + operation
			print(command)	
			
			exec(command)
			registers[name1] = eval(name1)
			registers[name2] = eval(name2)
			
			if registers[name1] > registers["highestValue"]:
				registers["highestValue"] = registers[name1]
			if registers[name2] > registers["highestValue"]:
				registers["highestValue"] = registers[name2]
			
		else:
			print("nomatch")
	return registers
	
registerValues = processRegisterInstructions(testArray)
print(registerValues)	

test_max = max(list(registerValues.values()))
test_max2 = registerValues["highestValue"]
if (test_max != 1):
	print("Test fail!")
	print(test_max)
else:
	print ("testArray succeeds")
	
if(test_max2 != 10):
		print("test fail")
		sys.exit()
else:
	print('test succeeds')
	
fileToRead = open('Day8input.txt','r')
message = fileToRead.read()
fileToRead.close()

registerValues = processRegisterInstructions(message.split("\n"))
print (max(list(registerValues.values())))
print(registerValues["highestValue"])
