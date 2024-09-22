import random


# Initialization
# 跑每一分鐘

num_customers = 100
simulate_time = 200
next_arrival_time = 0
next_depart_time = 0
next_event_time = 0
csc = int(0) # current_service_customer
cac = int(0) # current_arrive_customer
csq = int(0) # current_service_quantity
cqs = int(0) # current_quantity_system
cql = int(0) # current_quantity_line
system_number_arr = []
line_number_arr = []

# basic setting
interarrival_times = [random.randint(1, 6) for _ in range(num_customers)]
service_times = [random.randint(1, 6) for _ in range(num_customers)]

for i in range(simulate_time):

    if i == 0:
        cqs +=1 # system人數+1
        csq +=1 # service人數+1
        
        # 下次arrival/depart時間
        next_arrival_time += interarrival_times[cac]
        next_depart_time += service_times[csc]

        if next_arrival_time > next_depart_time:
            next_event_time = next_depart_time
        else:
            next_event_time = next_arrival_time

    elif i == next_event_time:
        # 確認下次事件是arrival or depart
        # both，各階段人數不變
        if next_arrival_time == next_depart_time:
            # arrival/depart 各加一號
            cac += 1
            csc += 1
            next_arrival_time = i + interarrival_times[cac]
            next_depart_time = i + service_times[csc]
            
        # arrival first
        elif next_arrival_time < next_depart_time:
            # system人數+1
            cqs += 1
            # 下一位arrival號碼
            cac += 1

            # next arrival time
            next_arrival_time = i + interarrival_times[cac]

            # service沒人，下次離開時間改變
            if csq == 0:
                csq +=1
                csc +=1
                next_depart_time = i + service_times[csc]
            # service有人，line加一人
            else:
                cql +=1


        # depart first
        elif next_arrival_time > next_depart_time:
            # system人數-1
            cqs -= 1
            # service人數-1
            csq -= 1
            
            # line上有人的話，進到service
            if cql > 0:
                cql -= 1
                csq += 1
                csc += 1
                # next depart time
                next_depart_time = i + service_times[csc]
            else:
                # 沒人的話，要等下一個arrival + service time
                next_depart_time = next_arrival_time + service_times[csc+1]

        if next_arrival_time > next_depart_time:
            next_event_time = next_depart_time
        else:
            next_event_time = next_arrival_time

    system_number_arr.append(int(cqs))
    line_number_arr.append(int(cql))

system_average = sum(system_number_arr)/simulate_time
line_average = sum(line_number_arr)/simulate_time

print(f"Average number of people in system:{system_average}")
print(f"Average number of people in line:{line_average}")
