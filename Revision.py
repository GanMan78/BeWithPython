
# Design object oriented python application which accepts N numbers from user, and perform below operarions.
# Display all even numbers
# Calculate the summation of all numbers
# Display all perfect numbers



class Numbers:
	
	def __init__(self,no=10):
		self.size=no
		self.arr=[]

	def __del__(self):
		print("Delocating the memory of object")
		del self.arr

	def Accept(self):
		print("Enter the elements:")
		for i in range(self.size):
			print("Enter number:",i+1)
			self.arr.append(int(input()))

	def Display(self):
		print("Elements of list are")
		for i in range(self.size):
			print(self.arr[i])
			
	def Summation(self):
		sum=0
		for i in range(self.size):
			sum=sum+self.arr[i]
			
		return sum
		
	def EvenDisplay(self):
		print("Even elements from list are :")
		for i in range(self.size):
			if (self.arr[i]%2)==0:
				print(self.arr[i])	

	def PerfectDisplay(self):
		sum=0
		for i in range(self.size):
			for j in range(1,int(self.arr[i]/2+1)):
				if (self.arr[i]%j)==0:
					sum=sum+j
			if sum==self.arr[i]:
				print(self.arr[i])
			sum=0

	def PrimeDisplay(self):
		Flag=False
		for i in range(self.size):
			for j in range(2,int(self.arr[i]/2)+1):
				if (self.arr[i]%j)==0:
					Flag=True
					break
			if Flag==False:
				print(self.arr[i])
			Flag=False

def main():
	print("Enter numbers of elements")
	value=int(input())
	
	obj1=Numbers(value)
	print(obj1.size)
	
	obj1.Accept()
	obj1.Display()
	ret=obj1.Summation()
	print("Summation of all numbers:",ret)

	obj1.EvenDisplay()
	print("Perfect numbers are:")
	obj1.PerfectDisplay()
	print("Prime numbers:")
	obj1.PrimeDisplay()
	
	# obj2=Numbers()  # object 2 by default 10 elements gheto due to constructor defination
	# obj2.Accept()
	# obj2.Display()
	
	del obj1
	
if __name__=="__main__":
	main()