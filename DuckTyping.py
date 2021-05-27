
class C:
	def LearnAndCode(self):
		print("Learning C programming")
		
class Cpp:
	def LearnAndCode(self):
		print("Learning C++ programming")
		
class Golang:
	def LearnAndCode(self):
		print("Learning Golang programming")
		
class Demo:
	pass
	
class Programmer:
	def Coding(self,language):
		language.LearnAndCode()
		
cobj=C()
cpobj=Cpp()
gobj=Golang()
dobj=Demo()

obj=Programmer()
obj.Coding(cobj)
obj.Coding(cpobj)
obj.Coding(gobj)
obj.Coding(dobj)