import random
import statistics


def turn_away_time():

    # number of random varaibles
    num_customers = 1000
    
    # 抵達間隔 ＆ 服務時間
    interarrival_times = [random.randint(1, 6) for _ in range(num_customers)]
    service_times = [random.randint(1, 6) for _ in range(num_customers)]
    
    
    # arrival    
    # waiting line
    # service
    # depart
    arrival_number = 0 
    service_number = 0 

    next_arrival_time = 0 
    next_depart_time = 0 
    next_event_time = 0 

    service_quantity = 0 # currently service number of people
    line_quantity = 0 # currently line number of people
    timer = 0 # 計時器

    while line_quantity < 4:
        if timer == 0:
            arrival_number += 1
            service_quantity += 1
            next_arrival_time += interarrival_times[arrival_number]
            next_depart_time += service_times[service_number]

            if next_arrival_time > next_depart_time:
                next_event_time = next_depart_time
            else:
                next_event_time = next_arrival_time
        elif timer == next_event_time:
            # 確認下次事件
            # both
            if next_arrival_time == next_depart_time:
                arrival_number += 1
                service_number += 1

                next_arrival_time += interarrival_times[arrival_number]
                next_depart_time = timer + service_times[service_number]
            # arrival first
            elif next_arrival_time < next_depart_time:
                arrival_number += 1
                next_arrival_time = timer + interarrival_times[arrival_number]

                # no one in service
                if service_quantity == 0:
                    service_quantity += 1
                    service_number += 1
                    
                    next_depart_time = timer + service_times[service_number]
                # someone in service
                else:
                    line_quantity += 1
            
            # depart first
            else:
                service_quantity -= 1

                # someone in line, then enter service immediately
                if line_quantity > 0:
                    service_quantity += 1
                    line_quantity -= 1
                    service_number += 1
                    
                    next_depart_time = timer + service_times[service_number]
                # no one in line
                else:
                    next_depart_time = next_arrival_time + service_times[service_number + 1]
        if next_arrival_time > next_depart_time:
            next_event_time = next_depart_time
        else:
            next_event_time = next_arrival_time
        timer += 1
        print(line_quantity)
    return timer


time_arr = []

for _ in range(1000):
    temp = turn_away_time()
    time_arr.append(temp)    

average_turn_away_time = statistics.mean(time_arr)
print(average_turn_away_time)
