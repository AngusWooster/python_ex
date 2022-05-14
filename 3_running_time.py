#!/usr/bin/python3


def run_timing():
    input_cnt = 0
    total_time = 0
    average_time = 0
    while True:
        t = input("input time(minutes) of running 10 km:")

        if (t == ''):
            break
        try:
            t = float(t)
            if (t < 0):
                print("unacceptable negative value")
                continue
            
            total_time += t
            input_cnt += 1

        except Exception as e:
                print("this is unacceptable value: ", e)

    if (input_cnt == 0):
        average_time = 0
    else:
        average_time = total_time / input_cnt
    print("run:", input_cnt, "average time is", average_time, "(min)")

run_timing()