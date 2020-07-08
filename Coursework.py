#F28PL - CW2 - Python

#Tomasz Mosak, tpm4
#F28PL Coursework PY1

#enjoy marking this as much as I loved coding it (sarcasm)

#####################################
#Question 1a
print()
print('Question 1')



def cadd(x,y):
		#takes the corrisponding values and adds them
	return (x[0]+y[0], x[1]+y[1])

#Tests
cadd((3,4), (5,6))
#expected output - (8,10)

cadd((0,-1),(1,3))
#expected output - (1,2)

def cmult(x,y):
		#multiplies complex numbers via taking certain values from the tuples
	return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])

#Tests
cmult((1,2),(3,4))
#expected output - (-5,10)

a = (-3,2,0)
b = (7,0,-1)
cmult(a,b)
#expected output - (-21,14)

#Question 1b

def fromcomplex(x):
	return (x.real, x.imag)

#Tests
fromcomplex(3+4j)
#expected output - (3.0, 4.0)
fromcomplex(0j)
#expected output - (0.0, 0.0)

def tocomplex(x):
    real = x[0]
    imag = x[1]*1j
    return (real + imag)

#Tests
x = (3.0, 4.0)
tocomplex(x)
#expected output - (3+4j)
x = (0.0, 0.0)
tocomplex(x)
#expected output - (0j)


################################################################################
#Question 2a
print()
print('Question 2')


def seqaddi(x, y):
	#loop for the amount of values
    for i in range(0,len(x)):
	#make x be the sum of the 2 corrisponding values
        x[i] = (x[i] + y[i])
	#print
    return(x)

#Tests
seqaddi([0,1,2],[1,2,3])
#expected output - [1,3,5]
seqaddi([0,1,3],[120,-20,13])
#expected output - [120,-19,16]
a = [-10, -20, 300]
b = [-50, 5 , -20]
seqaddi(a,b)
#expected output - [-60, -15, 280]

def seqmulti(x, y):
    for i in range(0,len(x)):
		#same as above but this time it multiplies
        x[i] = (x[i] * y[i])
    print(x)
    return(x)

#Tests
seqmulti([1,0,-9],[10,2,9])
#expected output - [10,0,-81]
seqmulti([3,-1,1000],[-1,1,0])
#expected output - [-3,-1,0]

#####################################
#Question 2b

def seqaddr(x, y, i = 0):
    if (i < len(x) or i < len(y)):
        return [x[i] + y[i]] + seqaddr(x, y, i + 1)
    else:
        return []

#Tests
seqaddr([0,1,2],[1,2,3])
#expected output - [1,3,5]
seqaddr([0,1,3],[120,-20,13])
#expected output - [120,-19,16]
		
def seqmultr(x, y, i = 0):
    if (i < len(x) or i < len(y)):
        return [x[i] * y[i]] + seqmultr(x, y, i + 1)
    else:
        return []
		
#Tests
seqmultr([1,0,-9],[10,2,9])
#expected output - [10,0,-81]
seqmultr([3,-1,1000],[-1,1,0])
#expected output - [-3,-1,0]

#####################################
#Question 2c

def seqaddl(x,y):
	return [a+b for a,b in zip(x,y)]
	
#Tests
seqaddl([0,1,2],[1,2,3])
#expected output - [1,3,5]
seqaddl([0,1,3],[120,-20,13])
#expected output - [120,-19,16]

def seqmultl(x,y):
	return [a*b for a,b in zip(x,y)]

#Tests
seqmultl([1,0,-9],[10,2,9])
#expected output - [10,0,-81]
seqmultl([3,-1,1000],[-1,1,0])
#expected output - [-3,-1,0]

################################################################################
#Question 3
print()
print('Question 3')

##Helper Fucntions

def seqadd(x,y):
	out = [x[i] + y[i] for i in range(len(x))]
	return out
seqadd([1,2,3], [1,2,3])

def matrixlength(x):
	j = 0
	for i in x:
		j += 1
	return j

def gethead(x):
	return x[0]	

###########################################
			
def ismatrix(a):
	#makes lenght equal to the amount of collumns
	length = len(a[0])
	for i in a:
	#checks if all the rows are the same lenght
		if(len(i) != length):
			return False
	return True


def matrixshape(a):
		#makes variables equal to the lenght of collumns and rows of the matrix and just returns that as the shape
	col = len(a[0])
	row = len(a)
	return (row, col)
	



def matrixadd(a, b):
	#creates empty list
	new = []
	#loops for the amount of items in rows
	for i in range(len(a)):
			#takes the corrisponding values of both matrix and add them, stick them into that empty list
			new.append(seqaddr(a[i],b[i]))
	return new
				
#Test
a = [[0,-1,2],[12,3,-9]]
b = [[-5,1,-1],[100,-3,10]]
matrixadd(a,b)
#expected output - [[-5,0,1],[112,0,1]]


def nullmatrix(x,y):
	listnothing = [0 for i in range(y)]
	#creates an empty matrix for preperation of multiplication
	matrixzero = [list(listnothing) for i in range(x)]
	return matrixzero
	


def matrixmult(x,y):
	matrixfinished = nullmatrix(len(x),len(y[0]))
	if (len(x[0])== len(y)):
		for i in range(0, len(x)):
			for j in range(0, len(y[0])):
				for k in range(0, len(y)):
					#takes both the inputs a,b goes through both the matrix's and multiplies them
					matrixfinished[i][j] += x[i][k] * y[k][j]
			return matrixfinished


#Test
a = [[1, 2, 3], [1, 2, 3]]
b = [[1, 2], [1, 2], [1, 2]]
matrixmult(a,b)
#expected output - [[6,12],[6,12]]

###############################################################################
#Question 4
print()
print('Question 4')

"""
Essay Questions

1.	Mutable types are types that will change depending on operations performed on them. Some of those are: lists, sets, dict types. 
What that means is that set(x) at the start of a computation might end up having completely different values within it at the end of the computation. An example of this would be:

x = [1,2]
y = x
y +=  [2,3]
print x will output [1,2,2,3] and not [1,2] because its mutable. Its changeable per say.

Another example of a mutable type is this:
Set = {‘greg’, ‘james’, ‘bob’}
X = set
x.add(‘tomasz’)
set
this shows {‘james’, ‘bob’, ‘tomasz’, ‘greg’} showing that sets are mutable types

Immutable types are basically just the opposite of mutable types. Its types which once set, stay the same. Some of those types are: bool, int, float and tuple. 
These allow the user to set x=5 and no matter of all other parts of the program x will remain 5 throughout the calculation of the program. A couple of examples of immutable types are:

x = 5
y= x
y += 2
print x will show 5 and not 7 because its immutable. It passes on its value to y however that value doesn’t change unless operations are performed specifically on x.

another example this time with tuples
x = (1,2,3)
y = x
y += (4,5)
print x will still show you the original tuple you created in line 1 whereas y is now a brand-new tuple.

2.	The main difference between integer and float types is the range that they compute. 
Integers deal with whole numbers (numbers without a fraction), so numbers such as -30, 0 , 22 are all integers whereas float type numbers are numbers that also include those fractions so 22.985 and 0.56 
are both float type numbers. Another major difference is that int is infinite precision and float isn’t! So if you were to multiply 2 huge numbers that were int type you’d get the exact answer, however, 
with float type numbers you would get something roughly right but not exact!


3.	The difference between assignment and equality is that as the name suggests, assignment assigns a value to a variable whereas equality checks for equality of 2 presented things. 

So an easy example to show the differences is:

a = 5
b = 5
 (this is assignment)
b == a (this outputs true because it checks for equality and both the variables have been assigned 5)
Identity unlike equality, it doesn’t check if the values are the same but instead checks if both the variables are pointing towards the same object in memory. Meaning that a == b but a is not y.

4.	Using the example provided of list(range(5**5**5)), what the program does is computes  the number first, then gives you a range which would be 0 and that number. 
However then getting the list of that range forces python to stick all the numbers in that range into a list! Trying that example will give you a memory error because python is unable to handle such vast numbers

5.	Slicing! What it does is slices a list or tuple into a smaller chunk. Lets say we have a list of 10 elements but for some reason we want the elements 2 – 4 
returned in a new list and this is done by specifying to python what slice we want (personally I think of a cake and asking a person where they want it cut as a metaphor for this) 
in this example we want slice[1:4] which gives us 2-4 because slicing index starts at 0 and 4 which is the 5th element in the list which we don’t include through slicing.

So, in the example given 
list(range(10**10) [10:10]) – This gives back an empty list because the starting pointer is also the end pointer which doesn’t get included in the slice
list(range(10**10))[10:10] – Gives an memory error due to the amount of numbers it must input into the list. Doesn’t even reach the slice part as python does the stuff inside the brackets first.

"""


###############################################################################
#Question 5
print()
print('Question 5')


def encdat(x):
	if (type(x) != str):
		x = str(x)
	return x

#Tests
encdat(5)
#expected output - '5'
encdat("hi")
#expected output - 'hi'

###############################################################################
#Question 6
print()
print('Question 6')


def fenc(n):
	if n==0:
	#if the number is = 0, add a [] 
		return []
	else:
		#if n is anything but 0 calls itself twice but also decrementing n towards 0 so it isnt just an infinite loop
		return [fenc(n-1),[fenc(n-1)]]
	

def fdec(n):
	if n == []:
		return 0
	elif n != []:
		return fdec(n[0]) +1
	#does the opposite of fenc
		
#Tests
x = fenc(3)
y = denc(x)
print(y)
#expected output - 3
x = fenc(10)
y = denc(x)
print(y)
#expected output - 10
	

###############################################################################
#Question 7
print()
print('Question 7')		
			
			
def cycleoflife(iterator):
	#makes an empty list
	life = []
	#makes a loop for each item within the cycle of life
	for items in iterator:
		yield items
		#adds the item to that empty list
		life.append(items)
	#once life has all the items
	while life:
		for element in life:
			#pop them back out
			yield element

#makes x the iterator within the cycleoflife function
x = cycleoflife(iter(["eat", "sleep", "code"]))

#endless cycle
next(x)

#you can also do this for it to spam it out automatically
while True:
	next(x)


#################################################################################
#Question 8
print()
print('Question 8')


def flatten(x):
	flat = []
	#creating a loop function within the flatten function to 
	#allow the program to go through all elements
	def loop(y):
		for i in y:
		#checks if current value is of type int or not
			if isinstance(i, list):
				loop(i)
			elif(type(i) == int):
			#if int adds it to a new list
				flat.append(i)
	loop(x)
	return flat
	
#Test
x = [[1,2],[3],[4],[],["cheeze"]]
flatten(x)
#expected output - [1,2,3,4]
	
	
#END ANSWER TO Question 8
################################################################################