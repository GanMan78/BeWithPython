

class Base1:
	def __init__(self):
		self.i=10
		self.j=20
		print("Inside Base1 constructor")
	
	def fun(self):
		print("Base1 fun")
		
class Base2:
	def __init__(self):
		self.x=30
		self.y=40
		print("Inside Base2 constructor")
		
	def fun(self):
		print("Base2 fun")
		
class Derived(Base1,Base2):
	def __init__(self):
		Base1.__init__(self)
		Base2.__init__(self)
		self.a=50
		self.b=60
		print("Inside Derived constructor")
		
def main():
	dobj=Derived()
	print(dobj.i)
	print(dobj.j)
	print(dobj.x)
	print(dobj.y)
	print(dobj.a)
	print(dobj.b)
	dobj.fun()
	
if __name__=="__main__":
	main()

