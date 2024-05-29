#By function only 

def cooking_time(needed_power, minutes, seconds, power):
    time = (minutes * 60 + seconds) * int(needed_power[:-1]) / int(power[:-1])
    time = int(time) + 1 if time %1 != 0 else int(time)
    return f"{time //60} minutes {time % 60} seconds"

print(cooking_time('600w',4,20,'800w'))

#By Math module

import math

def cooking_time(needed_power, minutes, seconds, power):
    t = math.ceil((60 * minutes + seconds) * int(needed_power[:-1]) / int(power[:-1]))
    return '%d minutes %d seconds' %(t // 60, t - t // 60 * 60)

print(cooking_time('600w',4,20,'800w'))
