import threading
import time

def worker(name, delay):
    for i in range(3):
        print(f"Thread {name}: Step {i+1}")
        time.sleep(delay)

# Create threads with args
t1 = threading.Thread(target=worker, args=("A", 1))
t2 = threading.Thread(target=worker, args=("B", 2))

t1.start()
t2.start()

t1.join()
t2.join()

print("Threads with arguments completed.")
