
# Inbuild function from module

def Substraction(no1,no2):
	print("5 : Inside Substraction")
	return no1-no2	

def SubDecorator(func_name):
	print("9 : Inside SubDecorator")
	def Updator(a,b):
		print("11 : Inside Updator")
		if a<b:     # if first parameter is small
			temp=a			# in python there is swapping shortcut as a,b=b,a
			a=b
			b=temp
		return func_name(a,b)
	return Updator
		
def main():
	print("20 : Inside main")
	Sub=SubDecorator(Substraction)
	
	print("Enter first number")
	no1=int(input())
	print("Enter second number")
	no2=int(input())
	
	ret=Sub(no1,no2)
	print("Substraction is ",ret)
	print("30 : End of main")

if __name__=="__main__":
	print("33 : Inside Starter")
	main()
	print("35 : End of starter")