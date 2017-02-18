def generatePyramid(n): 
	#function to generate array for pyramid with n levels
	x = []
	for i in range(1, n+1):
		x.append([j for j in range(i)])
	return x
		
def printPyramid(pyr):
	#prints every level of pyramid
	for level in pyr:
		print(level)
	
pyramid = generatePyramid(5)
printPyramid(pyramid)
