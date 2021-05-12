# Recursion : Calling the function from same function itself.

def DisplayI(no):
	for i in range(no):     # Iteration using for loop
		print("Hello")

def DisplayIW(no):          # Iteration using while loop
	while no!=0:
		print("Hello")
		no=no-1
	
def DisplayR(no):
	if no!=0:
		no=no-1
		print("Hello")
		DisplayR(no)        # Recursive call
		
def main():
	print("Enter the number of iterations")
	value=int(input())
	
	print("Calling iterative function with for loop")
	DisplayI(value)
	print("")
	
	print("Calling iterative function with while loop")
	DisplayIW(value)
	print("")

	print("Calling the recursaive function")
	DisplayR(value)
	print("")

if __name__=="__main__":
	main()