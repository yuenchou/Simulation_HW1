import numpy as np

def time_generator(beta):
    
    times = np.random.exponential(scale=beta)
    return times


num_delay_requires = 1000
Q_limit = 100   

sim_time = 0 # simulation clock

next_arrival_time = 0 
next_depart_time = 0 
next_event_time = 0 

server_status = 0 # current server status, 0 is idle, 1 is busy 
num_in_q = 0 # current number in queue
max_in_q = 0
total_custs_delay = 0 # cumulative number of delayed people

arrival_time_arr = []
service_time_arr = []
depart_time_arr = []
queue_service_time = [] # the service time of queue customer

# stop rule: 
# 1. The cumulative number of delayed people over requires
# 2. The number of people in the queue exceeds the limit
while total_custs_delay < num_delay_requires:

    interarrival_time = time_generator(1)
    service_time = time_generator(0.5)
    
    sim_time = next_event_time

    if next_event_time == 0:
        next_arrival_time += interarrival_time
        next_depart_time = next_arrival_time + service_time
        next_event_time = next_arrival_time

    else:
        # arrival
        if next_event_time == next_arrival_time:
            arrival_time_arr.append(next_arrival_time)
            
            # Is the server busy?
            if server_status == 0:
                server_status = 1
                service_time_arr.append(next_arrival_time)
            else:
                num_in_q += 1
                max_in_q = max(num_in_q, max_in_q)
                total_custs_delay += 1
                queue_service_time.append(service_time)
                if num_in_q > Q_limit:
                    print("Over queue limit")
                    break
            next_arrival_time += interarrival_time
        # depart
        elif next_event_time == next_depart_time:
            server_status = 0
            sim_time 
            depart_time_arr.append(next_depart_time)

            if num_in_q > 0:
                num_in_q -= 1
                server_status = 1
                service_time_arr.append(next_depart_time)

                next_depart_time += queue_service_time.pop(0)
            else:
                next_depart_time = next_arrival_time + service_time

    if next_arrival_time > next_depart_time:
        next_event_time = next_depart_time
    else:
        next_event_time = next_arrival_time
    
total_time_in_system = 0
max_total_time_system = 0

for i in range(len(depart_time_arr)):
    temp = depart_time_arr[i] - arrival_time_arr[i]
    total_time_in_system += temp
    max_total_time_system = max(max_total_time_system, temp)

max_delay_queue = 0
delay_over_one = 0

for i in range(len(depart_time_arr)):
    temp = service_time_arr[i] - arrival_time_arr[i]
    max_delay_queue = max(max_delay_queue, temp)
    if temp > 1:
        delay_over_one += 1

total_simulation_number = len(depart_time_arr)

time_average_system = total_time_in_system/sim_time
average_total_time = total_time_in_system/total_simulation_number
proportion_more_one = delay_over_one/total_simulation_number

print(f"The time-average number in the system : {np.round(time_average_system, 2)}")
print(f"The average total time in the system : {np.round(average_total_time, 2)}")
print(f"The maximum queue length : {np.round(max_in_q, 2)}")
print(f"The maximum delay in queue : {np.round(max_delay_queue, 2)}")
print(f"The maximum time in the system : {np.round(max_total_time_system, 2)}")
print(f"Proportion of waiting for more than one minute : {np.round(proportion_more_one, 2)}")