from datetime import datetime

OVERNIGHT_RATE = 3.90
SUNDAY_RATE = 2.90
NORMAL_RATE = 2.10

def is_overnight(day):
    return day.hour >= 22

def is_sunday(day):
    return day.weekday() == 6

def calculate_ride(distance, day):
    if not isinstance(distance, int) or distance < 0: raise Exception('Invalid distance parameter')
    if not isinstance(day, datetime): raise Exception('Invalid day parameter')
    if is_overnight(day):
        return distance * OVERNIGHT_RATE
    if is_sunday(day):
        return distance * SUNDAY_RATE
    return distance * NORMAL_RATE
