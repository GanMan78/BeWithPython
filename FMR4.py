# Accept N numbers from user and filterout only even numbers from that N numbers.
# After that add 2 in every even numbers
# After the addition of 2, perform summation of that modified numbers.

# Input [1,3,2,4,6,5,4]
# After map [4,6,8,6]
# After reduce 24

import functools


def main():
	arr=[]
	print("Enter numbers of elements")
	size=int(input())
	
	for i in range(size):
		print("Enter element number:",i+1)
		no=int(input())
		arr.append(no)
	
	print("Your entered data is:",arr)

	#newdata=filter(function_name,Data)
	newdata=list(filter(lambda no:(no%2==0),arr))        
	print("After filtering data is:",newdata)
	
	newdata1=list(map(lambda no: no+2,newdata))      
	print("After Map data is:",newdata1)
	
	result=functools.reduce(lambda no1,no2:no1+no2,newdata1)                
	print("After reduce result is:",result)
	
if __name__=="__main__":
	main()
