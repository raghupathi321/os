# Preemptive Shortest Job First (SRTF) Scheduling

def sjf_preemptive(processes, burst_time, arrival_time):
    n = len(processes)
    remaining_time = burst_time[:]  # Copy of burst times
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n

    complete = 0
    current_time = 0
    shortest = -1
    min_remaining = float('inf')
    check = False

    while complete != n:
        # Find process with minimum remaining time among arrived processes
        for i in range(n):
            if (arrival_time[i] <= current_time) and (remaining_time[i] > 0) and (remaining_time[i] < min_remaining):
                min_remaining = remaining_time[i]
                shortest = i
                check = True

        if not check:
            current_time += 1
            continue

        # Decrease remaining time
        remaining_time[shortest] -= 1
        min_remaining = remaining_time[shortest]
        if min_remaining == 0:
            min_remaining = float('inf')

        # If a process finishes
        if remaining_time[shortest] == 0:
            complete += 1
            check = False
            finish_time = current_time + 1
            completion_time[shortest] = finish_time
            turnaround_time[shortest] = finish_time - arrival_time[shortest]
            waiting_time[shortest] = turnaround_time[shortest] - burst_time[shortest]
            if waiting_time[shortest] < 0:
                waiting_time[shortest] = 0

        current_time += 1

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

sjf_preemptive(processes, burst_time, arrival_time)
