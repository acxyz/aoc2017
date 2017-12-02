import sys

def getLineSubTotalPhase1(int_list):
	return max(int_list) - min(int_list)

def getLineSubTotalPhase2(int_list):
	
	int_sorted = sorted(int_list)
	# print ("MAX: " + str(max(int_sorted)))
	# print(int_sorted)
	
	for  i in range(0 , len(int_sorted) -1) :
		break_now = False
		# print ("I: " + str(int_sorted[i]))
		for j in range(1 , len(int_sorted)) :
			# print ("J: " + str(int_sorted[j]))
			if i != j and 0 == int_sorted[j] % int_sorted[i]:
				diff = int(int_sorted[j]/int_sorted[i])
				# print ("BREAK")
				break_now = True
				break
		if break_now:
			break
	return diff
			
	
	
	
	
	
def processLine(line):
	
	ss_vals = list(map(int, line.split()))
	# diff = max(ss_vals) - min(ss_vals)
	# return diff
	if phase1:
		return getLineSubTotalPhase1(ss_vals)
	else:
		return getLineSubTotalPhase2(ss_vals)

#######################
#######################	
#######################
#######################



	# phase two:
	
	# It sounds like the goal is to find the only two numbers in each row where one evenly 
# divides the other - that is, where the result of the division operation is a whole 
# number. They would like you to find those numbers on each line, divide them, and add up 
# each line's result.
	



ss_data = """62	1649	1731	76	51	1295	349	719	52	1984	2015	2171	981	1809	181	1715
161	99	1506	1658	84	78	533	242	1685	86	107	1548	670	960	1641	610
95	2420	2404	2293	542	2107	2198	121	109	209	2759	1373	1446	905	1837	111
552	186	751	527	696	164	114	530	558	307	252	200	481	142	205	479
581	1344	994	1413	120	112	656	1315	1249	193	1411	1280	110	103	74	1007
2536	5252	159	179	4701	1264	1400	2313	4237	161	142	4336	1061	3987	2268	4669
3270	1026	381	185	293	3520	1705	1610	3302	628	3420	524	3172	244	295	39
4142	1835	4137	3821	3730	2094	468	141	150	3982	147	4271	1741	2039	4410	179
1796	83	2039	1252	84	1641	2165	1218	1936	335	1807	2268	66	102	1977	2445
96	65	201	275	257	282	233	60	57	200	216	134	72	105	81	212
3218	5576	5616	5253	178	3317	6147	5973	2424	274	4878	234	200	4781	5372	276
4171	2436	134	3705	3831	3952	2603	115	660	125	610	152	4517	587	1554	619
2970	128	2877	1565	1001	167	254	2672	59	473	2086	181	1305	162	1663	2918
271	348	229	278	981	1785	2290	516	473	2037	737	2291	2521	1494	1121	244
2208	2236	1451	621	1937	1952	865	61	1934	49	1510	50	1767	59	194	1344
94	2312	2397	333	1192	106	2713	2351	2650	2663	703	157	89	510	1824	125"""


# print ("This is the name of the script: ", sys.argv[0])
# print ("Number of arguments: ", len(sys.argv))
# print ("The arguments are: " , str(sys.argv))

phase1 = False

if len(sys.argv) > 1:
	if sys.argv[1] == "phase1":
		phase1 = True
		

ss_lines = ss_data.split('\n')
total = 0
for l in ss_lines:
	
	df = processLine(l);
	# print("Diff is " + str(df))
	total += df
	# print ("Total is " + str(total))

	# print()
	# print()
	# input("Press enter to continue...")
	

if (phase1 and total != 44216):
	raise ValueError("Unit test fails, expected 44216, total is " + str(total))
elif (not phase1 and total != 320):
	raise ValueError("Unit test fails, expected 320, total is " + str(total))
	
	
print ("Checksum is " + str(total))


	
	
