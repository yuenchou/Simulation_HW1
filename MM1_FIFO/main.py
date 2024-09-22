import random


# Initialization
num_customers = 100
simulate_time = 200
arrival_times = [0] * num_customers
start_times = [0] * num_customers
depart_times = [0] * num_customers
waiting_times = [0] * num_customers
people_in_line = 0
people_in_system = 0

# 抵達間隔 ＆ 服務時間
interarrival_times = [random.randint(1, 6) for _ in range(num_customers)]
service_times = [random.randint(1, 6) for _ in range(num_customers)]

# arrival    
# waiting line
# service
# depart

for i in range(num_customers):
    # first customer
    if i == 0:
        arrival_times[i] = 0
        start_times[i] = 0
        depart_times[i] = service_times[i]
        waiting_times[i] = 0
    # other customer
    else:
        arrival_times[i] = arrival_times[i - 1] + interarrival_times[i]
        start_times[i] = max(arrival_times[i], depart_times[i - 1])
        depart_times[i] = start_times[i] + service_times[i]
        if start_times[i] > arrival_times[i]:
            waiting_times[i] = start_times[i] - arrival_times[i]
    if arrival_times[i] < simulate_time:
        # 不是+1, 要算每個人在系統的時間, 才是系統平均人數
        people_in_system += (start_times[i] - arrival_times[i] + service_times[i])
        if start_times[i] < simulate_time:
            # 不是+1, 要算每個人等待時間, 才是line的平均人數
            people_in_line += (start_times[i] - arrival_times[i])

average_waiting_time = sum(waiting_times) / num_customers
average_people_in_line = people_in_line / simulate_time
average_people_in_system = people_in_system / simulate_time


print(f"Average waiting time for the 100 customers: {average_waiting_time} minutes")
print(f"Average number of people waiting in line during the first 200 minutes: {average_people_in_line}")
print(f"Average number of people in the system during the first 200 minutes: {average_people_in_system}")
