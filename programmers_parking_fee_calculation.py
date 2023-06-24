import math


def calc_time(t1, t2):
    h1 = int(t1.split(':')[0])
    m1 = int(t1.split(':')[1])
    h2 = int(t2.split(':')[0])
    m2 = int(t2.split(':')[1])

    return 60 * (h2 - h1) + (m2 - m1)


def calc_fee(t, fees):
    f = fees[1]
    if t > fees[0]:
        t -= fees[0]
        f += fees[3] * math.ceil(t / fees[2])
    return f


def solution(fees, records):
    answer = []

    stack_time = []
    # [learned] use lambda function
    records.sort(key = lambda x:x.split()[1])

    car = records[0].split()[1]
    for record in records:
        info = record.split()
        time = info[0]
        id = info[1]
        inout = info[2]

        if car == id:
            stack_time.append(time)
        else:
            t = 0
            if len(stack_time) % 2 != 0:
                stack_time.append('23:59')
            for i in range(0, len(stack_time), 2):
                t += calc_time(stack_time[i], stack_time[i+1])
            f = calc_fee(t, fees)
            answer.append(f)

            # new car
            car = id
            stack_time.clear()
            stack_time.append(time)

    # for last car
    # [caution] don't forget the last case
    t = 0
    if len(stack_time) % 2 != 0:
        stack_time.append('23:59')
    for i in range(0, len(stack_time), 2):
        t += calc_time(stack_time[i], stack_time[i + 1])
    f = calc_fee(t, fees)
    answer.append(f)

    return answer

# [more]
# - use Class if possible

