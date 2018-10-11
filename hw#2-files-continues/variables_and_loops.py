import numpy as np	#we use numpy for a lot of things

def main():
	i = 0		#declare i equal to 0
	n = 10		#declare n equal to 10
	x = 119.0	#float x, these have a
	
	#we can use humpy to quickly make arrays
	y= np.zeros(n,dtype=float) #declares 10 zeros
	
	#we can use for lopps tp iterate through a variable
	for i in range(n):	#1 in rage [0,n-1]
		y[i] = 2.0 * float(i) + 1.0 #set y  = 2i+1 a
		
	#we can iterate through the y elements one by one
	for y_element in y:
		print(y_element)
		
#execute the main function

if __name__== "__main__":
	main()