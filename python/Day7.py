import re
import sys

class disc:

	# weight = 0
	# name = ""
	
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
	# print(line)
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
				# print(" -- " + branch)
				d.children.append(branch)
			# print (d.children)
		discs[name] = d
	
	else:
		print ("nomatch")
			

# print (discs)

for disc_name, disc in discs.items(): 
	# print (disc_name)
	# print(disc.children)
	for c in disc.children:
		# print (c + '-' + disc_name)
		discs[c].parent = disc_name	

for disc_name, disc in discs.items():
	if disc.parent == None:
		ult_parent = disc
		print("ultimate parent is " + disc.name)

# for disc_name, disc in discs.items():
	# print (disc_name + " <- " + (disc.parent if disc.parent != None else ""))
	# for kid in disc.children:
		# print (" - " + kid)

def printWithKids(disc, indent):
	
	for i in range(indent):
		print ("\t", end="")
	print (disc.name + " [" + str(disc.weight) + "]")
	for c in disc.children:
		printWithKids(discs[c], indent + 1)
	# print("")

printWithKids(ult_parent,0)		
	
		
def calcWeight(disc):
	tot_weight = disc.weight
	# print ("tot weight is " + str(tot_weight))
	# print (disc.children)
	for kid in disc.children:
		kid_disc = discs[kid]
		tot_weight += calcWeight(discs[kid])
	return tot_weight

# ult_weight = calcWeight(ult_parent)

# print(ult_weight)

def findBad(disc):
	weights = {}		
	
	# weigh each child
	for c in disc.children:
		kid = discs[c]
		
		w = calcWeight(kid)
		kid.totalWeight = w
		print (kid.name + " weighs " + str(w))
		# print(w)
		if w in weights:
			weights[w].append(kid)
		else:
			weights[w] = []
			weights[w].append(kid)

	badDisc = None
	badWeight = 0
	for weight, weightList in weights.items():
		if len(weightList) == 1:
			badDisc = weightList[0]
			badWeight = weight
			print ("bad weight is " + str(badWeight))
			
		else:
			goodWeight = weight

	print(badWeight - goodWeight)
	if (badDisc != None):
		badDisc.excessWeight = badWeight - goodWeight
	return (badDisc)
	
	
	# if here, there are no unbalanced discs on top of this one.
	return None
			
# (bad , weight) = findBad(ult_parent)
# print (bad.name)			
		
def crawlTree(disc):
	bd = findBad(disc)
	if (bd == None):
		# this is the bad disc
		print (disc.name)
		print (" the excessWeight weight is " + str(disc.excessWeight))
		print (" the proper weight is " + str(disc.weight - disc.excessWeight))
	else:
		crawlTree(bd)
		
crawlTree (ult_parent)

	

