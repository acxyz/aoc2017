import re

class disc:
	children = []
	parent = None
	weight = 0
	name = ""
	
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
		
discs = {}	



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
		name = matches.group('name')
		weight = matches.group('weight')
		d = disc(name, weight)
		# print (" - " + name + " [" + weight + "]")
		
		branches = matches.group('branches')
		if branches:
			
			
			l = rgx_branches.findall(branches)
			
			for branch in l: 
				# print(" -- " + branch)
				d.children.append(branch)
	
		discs[name] = d
	
	else:
		print ("nomatch")
			

# print (discs)

for disc_name, disc in discs.items(): 
	for c in disc.children:
		discs[c].parent = disc	

for disc_name, disc in discs.items():
	if disc.parent == None:
		print("ultimate parent is " + disc.name)
		

		
		
		

