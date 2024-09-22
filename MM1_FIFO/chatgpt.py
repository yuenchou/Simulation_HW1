import random

# chatgpt+微調
# Number of customers
num_customers = 100

# Generate interarrival times and service times (uniformly distributed between 1 and 6 minutes)
interarrival_times = [random.randint(1, 6) for _ in range(num_customers)]
service_times = [random.randint(1, 6) for _ in range(num_customers)]

# Initialize variables for the simulation
arrival_times = [0] * num_customers
start_times = [0] * num_customers
depart_times = [0] * num_customers
waiting_times = [0] * num_customers

# Set the arrival time of the first customer to 0
arrival_times[0] = 0

# Simulate the arrival of each customer

for i in range(1, num_customers):
    # i的抵達時間 = (i - 1)抵達時間+間隔時間
    arrival_times[i] = arrival_times[i - 1] + interarrival_times[i]

# Simulate the service process
for i in range(num_customers):
    # The customer starts service when the server becomes available or when they arrive
    # 第一個customer從0開始進入
    # 開始服務時間:比較i的抵達時間和(i-1)的結束時間
    if i == 0:
        start_times[i] = arrival_times[i]
    else:
        start_times[i] = max(arrival_times[i], depart_times[i - 1])
    
    # The depart time is the start time plus the service time
    depart_times[i] = start_times[i] + service_times[i]
    
    # Waiting time is the time they waited in the queue (start time - arrival time)
    waiting_times[i] = start_times[i] - arrival_times[i]

# Calculate the average waiting time for the 100 customers
average_waiting_time = sum(waiting_times) / num_customers

# Calculate average number of people in line and in the system during the first 200 minutes
people_in_line = 0
people_in_system = 0
simulate_time = 200
for i in range(num_customers):
    if arrival_times[i] < simulate_time:
        # 不是+1, 要算每個人在系統的時間, 才是系統平均人數
        people_in_system += (start_times[i] - arrival_times[i] + service_times[i])  # Add the person entering the system
        # If their start time is after their arrival time, they waited in line
        if start_times[i] > arrival_times[i]:
            # 不是+1, 要算每個人等待時間, 才是line的平均人數
            people_in_line += (start_times[i] - arrival_times[i])

# Average number of people waiting in line during the first 200 minutes
average_people_in_line = people_in_line / simulate_time

# Average number of people in the system during the first 200 minutes
average_people_in_system = people_in_system / simulate_time

# Output the results
print(f"Average waiting time for the 100 customers: {average_waiting_time:.2f} minutes")
print(f"Average number of people waiting in line during the first 200 minutes: {average_people_in_line:.2f}")
print(f"Average number of people in the system during the first 200 minutes: {average_people_in_system:.2f}")