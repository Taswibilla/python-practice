#multithreading
import threading

def task():
    print("Thread running")

t1 = threading.Thread(target=task)
t1.start()
t1.join()
print("Thread finished")
#multiprocessing
from multiprocessing import Process

def task():
    print("Process running")

if __name__ == "__main__":
    p1 = Process(target=task)
    p1.start()
    p1.join()
    print("Process finished")
    