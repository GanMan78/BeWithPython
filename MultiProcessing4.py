
import os
import multiprocessing
from time import sleep

def Process1(no):
	print("Process1 is created")
	print("PID of process1 is : ",os.getpid())
	print("PID of parent process of process1 is : ",os.getppid())
	for i in range(no):
		sleep(1)
		print("Process-1 ",i)
	
def Process2(no):
	print("Process2 is created")
	print("PID of process2 is : ",os.getpid())
	print("PID of parent process of process2 is : ",os.getppid())
	for i in range(no):
		sleep(1)
		print("Process-2 ",i)

def main():
	value=100
	print("Inside main process")
	print("PID of current process is : ",os.getpid())
	print("PID of parent process of main is : ",os.getppid())
	
	P1=multiprocessing.Process(target=Process1,args=(value,))
	P2=multiprocessing.Process(target=Process2,args=(value,))

	P1.start()
	P2.start()
	
	P1.join()
	P2.join()
	
	print("End of main process")

if __name__=="__main__":
	main()