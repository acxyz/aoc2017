import re
import sys

class disc:

	weight = 0
	name = ""
	
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
		self.children = []
		self.parent = None
		
discs = {}	

file_name = sys.argv[1]

print(file_name)
# sys.exit()

f = open(file_name,'r')
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
		weight = int(matches.group('weight'))
		d = disc(name, weight)
		# print (" - " + name + " [" + weight + "]")
		
		branches = matches.group('branches')
		if branches:
			
			
			l = rgx_branches.findall(branches)
			
			for branch in l: 
				print(" -- " + branch)
				d.children.append(branch)
			print (d.children)
		discs[name] = d
	
	else:
		print ("nomatch")
			

# print (discs)

for disc_name, disc in discs.items(): 
	print (disc_name)
	print(disc.children)
	for c in disc.children:
		print (c + '-' + disc_name)
		discs[c].parent = disc_name	

for disc_name, disc in discs.items():
	if disc.parent == None:
		ult_parent = disc
		print("ultimate parent is " + disc.name)

for disc_name, disc in discs.items():
	print (disc_name + " <- " + disc.parent if disc.parent != None else "")

def calcWeight(disc):
	tot_weight = disc.weight
	# print ("tot weight is " + str(tot_weight))
	# print (disc.children)
	for kid in disc.children:
		kid_disc = discs[kid]
		if kid_disc.parent == disc:
			tot_weight += calcWeight(discs[kid])
	return tot_weight

ult_weight = calcWeight(ult_parent)

print(ult_weight)
		
		

