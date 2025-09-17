import os

pid = os.fork()
if pid == 0:
    print("Child process exiting...")
    os._exit(0)  # exit immediately
else:
    os.wait()
    print("Parent noticed child exit")
