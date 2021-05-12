# Accept N numbers from user and filterout only even numbers from that N numbers.
# After that add 2 in every even numbers
# After the addition of 2, perform summation of that modified numbers.

# Input [1,3,2,4,6,5,4]
# After map [4,6,8,6]
# After reduce 24

def CheckEven(no):
	if no%2==0:
		return True
	else:
		return False
		
def NewFilter(arr):
	brr=[]
	for i in range(len(arr)):
		if CheckEven(arr[i])==True:
			brr.append(arr[i])
		
	return brr

def NewMap(arr):
	for i in range(len(arr)):
		arr[i]=arr[i]+2
		
	return arr

def NewReduce(arr):
		sum=0
		for i in range(len(arr)):
			sum=sum+arr[i]
			
		return sum
		
def main():
	arr=[]
	print("Enter numbers of elements")
	size=int(input())
	
	for i in range(size):
		print("Enter element number:",i+1)
		no=int(input())
		arr.append(no)
	
	print("Your entered data is:",arr)

	newdata=NewFilter(arr)
	print("After filtering data is:",newdata)
	
	newdata1=NewMap(newdata)
	print("After Map data is:",newdata1)
	
	result=NewReduce(newdata1)
	print("After reduce result is:",result)
	
	
if __name__=="__main__":
	main()
