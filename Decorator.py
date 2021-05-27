
# Inbuild function from module

def Substraction(no1,no2):
	return no1-no2	

def main():
	print("Enter first number")
	no1=int(input())
	
	print("Enter second number")
	no2=int(input())
	
	ret=Substraction(no1,no2)
	print("Substraction is ",ret)

if __name__=="__main__":
	main()