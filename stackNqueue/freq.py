'''NFG function to find the next greater frequency 
element for each element in the array'''
def NFG(a, n): 
	
	if (n <= 0): 
		print("List empty") 
		return [] 

	# stack data structure to store the position 
	# of array element 
	stack = [0]*n 

	# freq is a dictionary which maintains the 
	# frequency of each element 
	freq = {} 
	for i in a: 
		freq[a[i]] = 0
	for i in a: 
		freq[a[i]] += 1

	# res to store the value of next greater 
	# frequency element for each element 
	res = [0]*n 

	# initialize top of stack to -1 
	top = -1

	# push the first position of array in the stack 
	top += 1
	stack[top] = 0
    
	# now iterate for the rest of elements 
    for i in range(1, n): 
        print(stack)

					
        if (freq[a[stack[top]]] > freq[a[i]]): 
            top += 1
            stack[top] = i 


        else: 
            
            while (top>-1 and freq[a[stack[top]]] < freq[a[i]]): 
                res[stack[top]] = a[i]
                top -= 1

            # now push the current element 
            top+=1
            stack[top] = i
	
	while (top > -1): 
		res[stack[top]] = -1
		top -= 1

	# return the res list containing next 
	# greater frequency element 
	return res 

# Driver program to test the function 
print(NFG([1,1,2,3,4,2,1],7)) 
