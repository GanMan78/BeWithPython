
# Inbuild function from module

def Substraction(no1,no2):
	return no1-no2	

def SubDecorator(func_name): # SubDecorator function is a Decorator in this code
	def Updator(a,b):
		if a<b:     # if first parameter is small
			temp=a			# in python there is swapping shortcut as a,b=b,a
			a=b
			b=temp
		return func_name(a,b)
	return Updator
		
def main():
	Sub=SubDecorator(Substraction)
	
	print("Enter first number")
	no1=int(input())
	print("Enter second number")
	no2=int(input())
	
	ret=Sub(no1,no2)
	print("Substraction is ",ret)

if __name__=="__main__":
	main()