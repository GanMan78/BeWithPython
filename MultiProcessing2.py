
import os
import multiprocessing

def Process1():
	print("Process1 is created")
	print("PID of process1 is : ",os.getpid())
	print("PID of parent process of process1 is : ",os.getppid())

def Process2():
	print("Process2 is created")
	print("PID of process2 is : ",os.getpid())
	print("PID of parent process of process2 is : ",os.getppid())

def main():
	
	print("Inside main process")
	print("PID of current process is : ",os.getpid())
	print("PID of parent process of main is : ",os.getppid())
	
	P1=multiprocessing.Process(target=Process1,args=())
	P2=multiprocessing.Process(target=Process2,args=())

	P1.start()
	P2.start()
	
	P1.join()
	P2.join()
	
	print("End of main process")

if __name__=="__main__":
	main()