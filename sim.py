from random import randint
MAX_METER = 913
METER_PER_RUN = 300
runs = 0
handles = 0
base_drop_rate = 0.001
rate_increase = None
use_kismets = False

def meter_off(runs,  MAX_METER, use_kismets):
    handles = 0
    for i in range(runs):
        x = randint(1,1000)
        if i % MAX_METER == 0 or x == 69:
            handles += 1
        elif x == 420 and use_kismets:
            handles += 1
    return handles

def meter_on(runs, MAX_METER, base_drop_rate, METER_PER_RUN, use_kismets):
    handles = 0
    final_drop_rate = base_drop_rate
    meter = 0
    for i in range(runs):
        final_drop_rate = base_drop_rate * (1+2*meter/MAX_METER)
        final_final_drop_rate = int(final_drop_rate*1000)
        #print(final_drop_rate)
        x = randint(final_final_drop_rate, 1000)
        if i % MAX_METER == 0:
            handles += 1
            meter = 0
            final_drop_rate = base_drop_rate
        if x == 999:
            handles += 1
            meter = 0
            final_drop_rate = base_drop_rate
        elif x == 998 and use_kismets:
            handles += 1
        else:
            meter += METER_PER_RUN
    return handles


while runs not in range(1,100000000):
        try:
            runs = int(input("How many runs do we simulate? "))
        except ValueError:
            print("Please Enter An Interger")

handles_off = meter_off(runs, MAX_METER, use_kismets)

handles_on = meter_on(runs, MAX_METER, base_drop_rate, METER_PER_RUN, use_kismets)
if handles_off == 0 or handles_on == 0:
    pass
else:
    print(F"With meter off it will take {runs/handles_off:.0f} runs to get a handle on average")
    print(F"With meter on it will take {runs/handles_on:.0f} runs to get a handle on average")
