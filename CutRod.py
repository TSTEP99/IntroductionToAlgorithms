

prices=[1, 5, 8, 9, 10, 17, 17, 20];

def recursive_cut_rod(prices,n):
	"""A recursive implementation of cut rod has an exponential runtime(O(2^n))"""
	if n==0: #Base Case- Returns 0 for rod of length
		return 0;
	maximum=float("-inf"); #initializes maximum value to negative infinity
	
	for i in range(0,n): #loops through finding the optimal sub solutions
		
		maximum=max(maximum,prices[i]+recursive_cut_rod(prices,n-i-1));# checks to see the maximum solution generated using recursion
	return maximum; # returns the maximum solution
		

def memoized_cut_rod_aux(prices,n,r):
	"""Helper function for the memoized_cut_rod_aux"""
	if n==0: #Base Case returns of 0;
		return 0;
	
	if r[n-1]>=0: #If the value is already in the table returns it
		return r[n];
	else:
		maximum=float("-inf"); #set maximum to negative infinity 
		for i in range(0,n): #loops through to calculate
			maximum=max(maximum,prices[i]+memoized_cut_rod_aux(prices,n-i-1));
		r[n-1]=maximum; #sets the new calculated value to the maximum value
		return maximum;
			
	
def memoized_cut_rod(prices,n):
	"""A top down memoized approach to rot cutting"""
	r=[float("-inf") for i in range(n)]; #initializes array for helper function
	
	return memoized_cut_rod_aux(prices,n,r); #Returns the values of the auxilary function
	
def bottom_up_cut_rod(prices,n):
	"""Bottom up memoized approach torod cutting"""
	r=[ float("-inf") for i in range(n+1)] #initializes array to track cost
	r[0]=0; # initlizas rod of length 0 to price of length 0
	for i in range(1,n+1):# loops through rods from 1 to n
		maximum=float("-inf")#set maximum to negative infinity
		for j in range(1,i+1): # computes max rpice for rod that is cut up
			maximum=max(maximum,prices[j-1]+r[i-j])
		r[i]=maximum #sets r to maximum value
	return r[n]; # returns the maximum value
			
def extended_bottom_up_cut_rod(prices,n):
	"""Bottom up approach that allows the optimal solution to be reordered"""
	s=[float("-inf") for i in range(n+1)]; #array for the optimal cut
	r=[float("-inf") for i in range(n+1)]; #intilizes array to track cost
	r[0]=0; # initializes length of 0 to 0 cost
	for i in range(1,n+1):
		maximum=float("-inf"); #Initializes maximum value to negative infinity
		for j in range(1,n+1):
			if(prices[j-1]+r[i-j]>maximum):# changes maximum value based on calculated cost
				maximum=prices[j-1]+r[i-j];
				s[i]=j;
			
		r[i]=maximum; #sets stored value to maximum price
	return r,s;

def print_cut_rod(prices,n):
	"""Prints the optimal solution returned by extened_bottum_cut_up"""
	r,s=extended_bottom_up_cut_rod(prices,n) #loops through optimal solution to print it
	while n>=1: # Prints until the pieces
		print(s[n],end=" "); #prints the piece size out onto the same line
		n=n-s[n];

print_cut_rod(prices,len(prices)); #prints the solution for a rod of length 8 given the prices above

			