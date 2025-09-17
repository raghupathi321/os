def round_robin(processes, arrival_time, burst_time, quantum):
    n = len(processes)
    rem_bt = burst_time[:]  # Remaining burst times
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n

    t = 0  # Current time
    queue = []
    visited = [False] * n
    completed = 0

    while completed < n:
        # Add newly arrived processes to the queue
        for i in range(n):
            if arrival_time[i] <= t and not visited[i]:
                queue.append(i)
                visited[i] = True

        if not queue:
            t += 1  # CPU is idle
            continue

        idx = queue.pop(0)  # Take process from queue

        if rem_bt[idx] > quantum:
            t += quantum
            rem_bt[idx] -= quantum
        else:
            t += rem_bt[idx]
            completion_time[idx] = t
            turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
            waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
            rem_bt[idx] = 0
            completed += 1

        # Add new arrivals after execution
        for i in range(n):
            if arrival_time[i] <= t and not visited[i]:
                queue.append(i)
                visited[i] = True

        # If the process still has remaining burst time, put it back in queue
        if rem_bt[idx] > 0:
            queue.append(idx)

    # Print results
    print("\n--- Round Robin Scheduling ---")
    print("Process\tAT\tBT\tCT\tTAT\tWT")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

    print(f"\nAverage Waiting Time: {sum(waiting_time)/n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_time)/n:.2f}")


# Input Handling
n = int(input("Enter number of processes: "))
processes, arrival_time, burst_time = [], [], []

for i in range(n):
    processes.append(f"P{i+1}")
    arrival_time.append(int(input(f"Enter arrival time for process P{i+1}: ")))
    burst_time.append(int(input(f"Enter burst time for process P{i+1}: ")))

quantum = int(input("Enter time quantum: "))

round_robin(processes, arrival_time, burst_time, quantum)
