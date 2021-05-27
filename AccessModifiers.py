
# Public   we can directly define without any underscore
# Protected		need to specify with one underscore
# Private		need to specify with two underscore

class Base:
	def __init__(self):
		self.no1=11			# public member
		self._no2=21		# protected member
		self.__no3=51		# private member
		
	def fun(self):			# public method
		print(self.no1,self._no2,self.__no3)
	
	def _fun(self):			# protected method
		print(self.no1,self._no2,self.__no3)
		
	def __fun(self):		# private method
		print(self.no1,self._no2,self.__no3)
				
class Derived(Base):
	def __init__(self):
		Base.__init__(self)
		
	def gun(self):
		print(self.no1)
		print(self._no2)
		#print(self.__no3)	# Not allowed-private member
		self.fun()
		self._fun()
		#self.__fun()		# Not allowed-private method
		
		
def main():
	bobj=Base()
	print(bobj.no1)
	print(bobj._no2)
	#print(bobj.__no3)		# not allowed as it is a private variable
	bobj.fun()
	bobj._fun()
	#bobj.__fun()			# Not allowed-private method
	
	dobj=Derived()
	dobj.gun()
	
if __name__=="__main__":
	main()