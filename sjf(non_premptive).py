# Shortest Job First (SJF) - Non-Preemptive Scheduling

def sjf_non_preemptive(processes, burst_time, arrival_time):
    n = len(processes)
    completed = [False] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    
    current_time = 0
    completed_count = 0

    while completed_count < n:
        # Select process with minimum burst time among arrived processes
        idx = -1
        min_bt = float('inf')

        for i in range(n):
            if arrival_time[i] <= current_time and not completed[i]:
                if burst_time[i] < min_bt:
                    min_bt = burst_time[i]
                    idx = i

        if idx == -1:  
            # No process has arrived yet, move time forward
            current_time += 1
            continue

        # Process selected
        current_time += burst_time[idx]
        completion_time[idx] = current_time
        turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
        waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
        completed[idx] = True
        completed_count += 1

    # Print results
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

sjf_non_preemptive(processes, burst_time, arrival_time)
