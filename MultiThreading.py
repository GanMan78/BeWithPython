
import os
import threading
from time import sleep

def Thread1(no):
	print("Thread1 is created")
	print("PID of Thread1 is : ",os.getpid())
	for i in range(no):
		sleep(1)
		print("Thread-1 ",i)
	
def Thread2(no):
	print("Thread2 is created")
	print("PID of Thread2 is : ",os.getpid())
	for i in range(no):
		sleep(1)
		print("Thread-2 ",i)

def main():
	value=10
	print("Inside main thread")
	print("PID of current process is : ",os.getpid())
	print("PID of parent process of main is : ",os.getppid())
	
	T1=threading.Thread(target=Thread1,args=(value,))
	T2=threading.Thread(target=Thread2,args=(value,))

	T1.start()
	T2.start()
	
	T1.join()
	T2.join()
	
	print("End of main process")

if __name__=="__main__":
	main()