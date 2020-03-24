#Importing metaphone Library.
from metaphone import *

import enchant

import re

from difflib import *

def lcs_len(x, y):
    """This function returns length of longest common sequence of x and y."""
 
    if len(x) == 0 or len(y) == 0:
        return 0
 
    xx = x[:-1]   # xx = sequence x without its last element    
    yy = y[:-1]
 
    if x[-1] == y[-1]:  # if last elements of x and y are equal
        return lcs_len(xx, yy) + 1
    else:
        return max(lcs_len(xx, y), lcs_len(x, yy))


def prefix_match(x,y):
	
	if len(x) == 0 or len(y) == 0:
		return 0
	
	if x[0] == y[0]:
		return prefix_match(x[1:],y[1:]) + 1
	else :
		return 0

def suffix_match(x,y):
	
	if len(x) == 0 or len(y) == 0:
		return 0
	
	if x[-1] == y[-1]:
		return suffix_match(x[:-1],y[0:-1]) + 1
	else :
		return 0
		
def giveAvg(x,y):
	return (float((len(x)+len(y)))/2)


#Selecting the Dictionary.
d = enchant.Dict("en_US")                

try:
    #with open('englishnew.txt', 'rU') as infile:
    with open('dict/american-english', 'rU') as infile:
        wordSet = set(line.strip() for line in infile)
except IOError:
       print ("error opening file\n")


"""
str1 = "helo there how are you"
liststr = str1.split()
for i in liststr:
	print i
"""

flagReplace = 0
csetMain = []
csetFlag = []


strInput = raw_input('Enter your text: ')

str = re.sub("[\.,!?]+", " ", strInput)
#print str
#str = str.replace(",", " ")

print ("\n----------- Confusion Set Generation Started ---------------\n")

for str2 in str.split():
	
	str2 = str2.strip()
	
	if(d.check(str2) == False):
		cset = []
		cset2 = []
		strlist = []
		
		
		strNew = str2
		strNew = re.sub("10", "ten", strNew)
		for j in strNew:
			if(j.isdigit() == False):
				strlist.append(j)
			else:
				if(j=='1'):
					strlist.append('one')
				elif(j=='2'):
					strlist.append('two')
				elif(j=='3'):
					strlist.append('three')
				elif(j=='4'):
					strlist.append('four')
				elif(j=='5'):
					strlist.append('five')
				elif(j=='6'):
					strlist.append('six')
				elif(j=='7'):
					strlist.append('seven')
				elif(j=='8'):
					strlist.append('eight')
					#strlist.append('ate')
				elif(j=='9'):
					strlist.append('nine')
		
		str3 = ''.join(strlist)
		#print str3
		strNew = str3
		ustr = (strNew.decode('unicode-escape'))
		#ustr = repr(str.decode('unicode-escape'))
		#print ustr
		#print dm(ustr)


		for x in wordSet:
			ux = (x.decode('unicode-escape'))
			
			if dm(ux) == dm(ustr):
				#print "Word With similar phonetic Found" , x
				cset.append(x)

		if strNew in cset:
			flagReplace = 1
			print ('Now the word \'%s\' is in dictionary after replacement\n')%str2
			csetFlag.append(1)
			csetMain.append([strNew])
			continue

		#print cset
		
		cc = get_close_matches(strNew, cset,5,0.55)
		print ('Confusion Set of %s: ')%str2
		print (cc)
		print ('\n')
		csetMain.append(cc)
		csetFlag.append(1)
	else:
		print ('The word \'%s\' is in Dictionary \n')%str2
		csetFlag.append(0)
		csetMain.append([])

print ("----------- Confusion Set Generation Ended ---------------\n")



myvar = 0;

for str2 in str.split():
	
	str2 = str2.strip()
	
	seqMatch = 0
	lcsMatch = 0
	suffixMatch = 0
	prefixMatch = 0
	rank = 0
	rankIndex = 0
	
	if csetFlag[myvar] == 1:
		
		strlist = []
		strNew = str2
		strNew = re.sub("10", "ten", strNew)
		for j in strNew:
			if(j.isdigit() == False):
				strlist.append(j)
			else:
				if(j=='1'):
					strlist.append('one')
				elif(j=='2'):
					strlist.append('two')
				elif(j=='3'):
					strlist.append('three')
				elif(j=='4'):
					strlist.append('four')
				elif(j=='5'):
					strlist.append('five')
				elif(j=='6'):
					strlist.append('six')
				elif(j=='7'):
					strlist.append('seven')
				elif(j=='8'):
					strlist.append('eight')
					#strlist.append('ate')
				elif(j=='9'):
					strlist.append('nine')
		
		str3 = ''.join(strlist)
		#print str3
		strNew = str3
		
		print ('For Word \'%s\' we have the following :\n')%str2
		
		csetmyvar = 0
		
		for setitem in csetMain[myvar]:
			
			seqMatch = SequenceMatcher(None, setitem, strNew).ratio()
			lcsMatch = lcs_len(setitem, strNew)/giveAvg(setitem,strNew)
			prefixMatch = prefix_match(setitem, strNew)/giveAvg(setitem,strNew)
			suffixMatch = suffix_match(setitem, strNew)/giveAvg(setitem,strNew)
			
			rank11 = seqMatch + lcsMatch + prefixMatch + suffixMatch ;
			if rank11 > rank :
				rank = rank11
				rankIndex = csetmyvar
			else:
				csetmyvar = csetmyvar + 1
		
		print ('Candidate Selected = \'%s\' \n')%csetMain[myvar][rankIndex] 
	else:
		print ('The word \'%s\' is in Dictionary \n')%str2
		myvar = myvar + 1
		


