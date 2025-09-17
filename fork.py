import os

pid = os.fork()
if pid == 0:  # Child process
    print(f"Child process with PID {os.getpid()}")
else:  # Parent process
    print(f"Parent process with PID {os.getpid()}, child PID = {pid}")
