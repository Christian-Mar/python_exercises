from time import time

def time_function():
    now = time()  # import time from 1970 in seconds
    print(now)
    day = 60 * 60 * 24  # 1 day = 60 seconds * 60 minutes * 24 hours
    days = now // day
    years = days / 365  # check with a more comprehensible number
    print(years)
    time_after_days = now % day # base to calculate the time today
    print(time_after_days)
    hours = time_after_days // (60 * 60)
    hours_remainder = time_after_days % (60 * 60)
    minutes = hours_remainder // 60
    minutes_remainder = hours_remainder % 60
    seconds = minutes_remainder % 60

    return f"Sinds begin 1970 zijn er {int(days)} dagen verstreken. Op dit moment is het {int(hours)}:{int(minutes)}:{int(seconds)}"

print(time_function())
