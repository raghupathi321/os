import os

pid = os.fork()
if pid == 0:
    print("Child replacing itself with `ls` command...")
    os.execlp("ls", "ls", "-l")  # replace child with ls command
else:
    os.wait()
