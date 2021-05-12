# Recursion : Calling the function from same function itself.


def Addition(data):
	sum=0
	for i in range(len(data)):sum=sum+data[i]
	return sum

i=0
sum=0
def AdditionR(data):
	global i
	global sum
	if i<(len(data)):
		sum=sum+data[i]	
		i=i+1
		AdditionR(data)
	return sum

def main():
	arr=[]
	size=int(input("Enter the size of array"))
	for i in range(size):arr.append(int(input()))
	
	print("Data is:",arr)
	
	print("Addition is:", Addition(arr))
	print("Addition recursion is:", AdditionR(arr))

if __name__=="__main__":
	main()