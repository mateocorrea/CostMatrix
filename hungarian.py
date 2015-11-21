import random

def createMatrix(rows, columns, max):
	matrix = [[0]*columns for i in range(columns)]
	for a in matrix:
		for x in range (0, len(a)):
			a[x] = random.randint(1,max)
	return matrix #[[random.randint(0,max)]*columns for i in range(rows)]

def min_in_col(matrix, column): 
	minimum = (matrix[0])[column]
	for a in matrix:
		if a[column] < minimum:
			minimum = a[column]
	return minimum

def simplify(matrix):
	for a in matrix:
		min_in_row = min(a)
		for x in range (0, len(a)):
			a[x] = a[x] - min_in_row
	mins = list()
	for x in range(0, len(matrix)):
		mins.append(min_in_col(matrix, x))
	for a in matrix:
		for x in range (0, len(a)):
			a[x] = a[x] - mins[x]
	return matrix

def numZeros(matrix, line, row=True):
	zeros = 0
	if row == True:
		for a in matrix[line]:
			if a == 0:
				zeros = zeros + 1
	else:
		for a in matrix:
			if a[line] == 0:
				zeros = zeros + 1
	return zeros

def crossOut(matrix):
	crosses = 0
	while(something): # matrix contains uncrossed out zeros
		zeros = 0;
		max_zeros = -1;
		for x in range(0, len(matrix)):
			if (numZeros(matrix, x) > zeros) and not crossedOut(matrix, x):
				zeros = numZeros(matrix, x)
				max_zeros = x
			if (numzeros(matrix, x, row=False) > zeros) and not crossedOut(matrix, x, row=False):
				zeros = numzeros(matrix, x, row=False)
				max_zeros = x + len(matrix)
	return crosses

def crossedOut(matrix, line, row=True):
	return containsZero(matrix, line, row)

matrix = createMatrix(3, 3, 10)
print(matrix)
line_matrix = [(0,0,0), (0,0,0), (0,0,0)]
simplify(matrix)
print(matrix)
print(numZeros(matrix, 1, row=False))

















def containsZero(matrix, line, row=True):
	if row == True:
		for a in matrix[line]:
			if a == 0:
				return True
	else:
		for a in matrix:
			if a[line] == 0:
				return True
	return False



#good, not necessary
def min_in_row(matrix, row):
	minimum = (matrix[row])[0]
	for a in matrix[row]:
		if a < minimum:
			minimum = a
	return minimum
