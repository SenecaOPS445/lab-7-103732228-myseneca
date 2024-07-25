#!/usr/bin/env python3
# Student ID: mmateo2/103732228
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    t1_seconds = time_to_sec(t1)
    t2_seconds = time_to_sec(t2)
    total_seconds = t1_seconds + t2_seconds
    return sec_to_time(total_seconds)


def change_time(time, seconds):
    """Convert time object to seconds since midnight"""
    current_seconds = time_to_sec(time)
    new_seconds = current_seconds + seconds
    """Convert new seconds back to time object"""
    return sec_to_time(new_seconds)

def time_to_sec(time):
    """Calculate total minutes"""
    minutes = time.hour * 60 + time.minute
    """Calculate total seconds"""
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    """Create a new time object"""
    time = Time()
    """Calculate minutes and seconds using divmod"""
    minutes, time.second = divmod(seconds, 60)
    """Calculate hours and minutes using divmod"""
    time.hour, time.minute = divmod(minutes,60)
    return time

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True