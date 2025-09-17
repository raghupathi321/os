import os

pid = os.fork()
if pid == 0:
    print("Child process running...")
    os._exit(0)  # child exits
else:
    finished_pid, status = os.wait()
    print(f"Parent: Child {finished_pid} finished with status {status}")
