import os

print("Current nice value:", os.nice(0))
os.nice(5)  # increase niceness (lower priority)
print("New nice value:", os.nice(0))
