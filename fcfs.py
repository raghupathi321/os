# FCFS Scheduling Algorithm with Dynamic Input

def fcfs(processes, burst_time, arrival_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n

    # Sort processes by arrival time
    processes = [x for _, x in sorted(zip(arrival_time, processes))]
    burst_time = [x for _, x in sorted(zip(arrival_time, burst_time))]
    arrival_time = sorted(arrival_time)

    # First process
    completion_time[0] = arrival_time[0] + burst_time[0]
    turnaround_time[0] = completion_time[0] - arrival_time[0]
    waiting_time[0] = turnaround_time[0] - burst_time[0]

    # Remaining processes
    for i in range(1, n):
        if completion_time[i-1] < arrival_time[i]:
            completion_time[i] = arrival_time[i] + burst_time[i]  # CPU idle
        else:
            completion_time[i] = completion_time[i-1] + burst_time[i]

        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

    print(f"\nAverage Waiting Time: {sum(waiting_time)/n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_time)/n:.2f}")


# Input handling
n = int(input("Enter number of processes: "))
processes, burst_time, arrival_time = [], [], []

for i in range(n):
    processes.append(f"P{i+1}")
    arrival_time.append(int(input(f"Enter arrival time for process P{i+1}: ")))
    burst_time.append(int(input(f"Enter burst time for process P{i+1}: ")))

fcfs(processes, burst_time, arrival_time)
