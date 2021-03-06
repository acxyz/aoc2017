import re
import sys

class Disc:
	
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
		self.children = []
		self.parent = None

def getDiscsFromFile(file_name):
		
	f = open(inputFile,'r')
	message = f.read()
	f.close()

	lines = message.split("\n")

	# okseah (78)
	# ebmcu (30) -> glsrg, ckhip, rqhhyc, jjvxxtt, rdnpoms
	# wuybunc (54)

	# use named group:
	rgx_line = re.compile(r"^(?P<name>\w+) \((?P<weight>\d+)\)( ->(?P<branches>( \w+\,?)+))?" )
	rgx_branches = re.compile(r"\w+")

	for line in lines:

		matches = rgx_line.match(line)

		if matches:
			name = matches.group('name')
			weight = int(matches.group('weight'))
			d = Disc(name, weight)
			
			branches = matches.group('branches')

			if branches:
				l = rgx_branches.findall(branches)
				
				for branch in l: 
					d.children.append(branch)

			discs[name] = d
		
		else:
			print ("nomatch")
				
	for disc_name, disc in discs.items(): 
		for c in disc.children:
			discs[c].parent = disc_name	
	return discs
	
def printWithKids(disc, indent):
	
	for i in range(indent):
		print ("\t", end="")
		
	print (disc.name + " [" + str(disc.weight) + "]")
	
	for c in disc.children:
		printWithKids(discs[c], indent + 1)
		
def calcWeight(disc):

	tot_weight = disc.weight

	for kid in disc.children:
		tot_weight += calcWeight(discs[kid])

	return tot_weight

def findBadChild(disc):

	# key = weight / value = list of children who weigh that much
	# off-balance child will be the one in a list of one. 
	# I guess there must always be more than one "correct" disc or this won't work
	# That seems to be the case in the puzzle, but must it be? Maybe it could be
	# inferred from the siblings of this disc? 
	weights = {}		
	
	# weigh each child
	for c in disc.children:
		kid = discs[c]
		
		w = calcWeight(kid)
		kid.totalWeight = w
		print (kid.name + " weighs " + str(w))

		if w in weights:
			weights[w].append(kid)
		else:
			weights[w] = []
			weights[w].append(kid)
	
	print ("")
	badDisc = None
	badWeight = 0

	for weight, weightList in weights.items():
		
		if len(weightList) == 1:
			badDisc = weightList[0]
			badWeight = weight			
		else:
			goodWeight = weight

	if (badDisc != None):
		badDisc.excessWeight = badWeight - goodWeight
	return (badDisc)
	
			
def crawlTree(disc):
	bd = findBadChild(disc)
	if (bd == None):
		# this is the bad disc
		print (disc.name)
		print (" the excessWeight weight is " + str(disc.excessWeight))
		print (" the proper weight is " + str(disc.weight - disc.excessWeight))
	else:
		crawlTree(bd)

discs = {}	

inputFile = sys.argv[1]

print(inputFile)

discs = getDiscsFromFile(inputFile)	
			
# solve part 1:		
for disc_name, disc in discs.items():
	if disc.parent == None:
		ult_parent = disc
		print("ultimate parent is " + disc.name)

printWithKids(ult_parent,0)				
crawlTree (ult_parent)

	

