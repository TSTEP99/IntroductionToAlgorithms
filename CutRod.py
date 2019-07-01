

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
	r=[float("-inf") for i in range(n)]; #initializes array for helper function
	
	return memoized_cut_rod_aux(prices,n,r); #
	
def bottom_up_cut_rod(prices,n):
	r=[ float("-inf") for i in range(n+1)]
	r[0]=0;
	for i in range(1,n+1):
		maximum=float("-inf")
		for j in range(1,i+1):
			maximum=max(maximum,prices[j-1]+r[i-j])
		r[i]=maximum
	return r[n];
			
def extended_bottom_up_cut_rod(prices,n):
	s=[float("-inf") for i in range(n+1)];
	r=[float("-inf") for i in range(n+1)];
	r[0]=0;
	for i in range(1,n+1):
		maximum=float("-inf");
		for j in range(1,n+1):
			if(prices[j-1]+r[i-j]>maximum):
				maximum=prices[j-1]+r[i-j];
				s[i]=j;
			
		r[i]=maximum;
	return r,s;

def print_cut_rod(prices,n):
	r,s=extended_bottom_up_cut_rod(prices,n)
	while n>=1:
		print(s[n],end=" ");
		n=n-s[n];

print_cut_rod(prices,len(prices));

			