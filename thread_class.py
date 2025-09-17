import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
    
    def run(self):
        for i in range(3):
            print(f"{self.name}: Step {i+1}")
            time.sleep(self.delay)

# Create objects of thread class
t1 = MyThread("Thread-1", 1)
t2 = MyThread("Thread-2", 2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Custom thread class execution finished.")
