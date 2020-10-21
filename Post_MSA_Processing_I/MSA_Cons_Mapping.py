############################################
# Describe what it does here...

#


############################################
# Imports
import numpy as np 
import pandas as pd 


############################################
filename='Blossum62_Matrix.txt'


# input = np.loadtxt("Blossum62_Matrix.txt", dtype='i', delimiter=',', comments='#')
# print(input)


# data = pd.read_csv('Blossum62_Matrix.txt', sep=",", header=None)
# print(data)


# data = np.loadtxt(filename, delimiter=',', skiprows=7)

files=[filename]

for i in files:
    filename=i
    N=5
    # Method 1:
    out=[]
    with open(filename, "r") as f: # important to use with command when dealing with files
        counter = 0
        # print('File: %s' % filename)
        for line in f:
            counter += 1
            out.append(line)

matrix=[]
for i in out:
	if '#' in i:
		continue
	else:
		matrix.append(i)
		# print(i)
# This is just a clean version of the matrix

# still need to build this into a numpy array

print(matrix)

for i in matrix:
