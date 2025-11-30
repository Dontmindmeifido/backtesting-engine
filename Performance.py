import numpy
import math 

def parse_time(timeframe):
    '''
    Return time in seconds
    '''

    # Constants
    time = {
        "second": 60,
        "minute": 60,
        "hour": 24,
        "day": 1,
        "week": 1/7,
        "month": 1/30
    }

    
    temp = 1
    for key in time.keys():
        if key != timeframe:
            temp *= time[key]
        elif key == timeframe:
            return temp
        
    return 0
    
def sharpe(cumulative_return, timeframe):
    discrete_return = [cumulative_return[i] - cumulative_return[i - 1] for i in range(len(cumulative_return))]

    total_return = cumulative_return[-1]
    standard_deviation = numpy.std(discrete_return)

    return total_return / (standard_deviation * math.sqrt(parse_time(timeframe) / 60 * 60 * 24 * 256))


