import resource

usage = resource.getrusage(resource.RUSAGE_SELF)
print("Max resident set size (approx memory usage):", usage.ru_maxrss, "KB")

# brk() (in Python, you can’t call brk() directly, but you can simulate memory allocation with resource or just use malloc in C. Best demo is with resource.getrusage() but I’ll show low-level.)
