__author__ = "Josh Hansen <josh@skwash.net>"
__date__ = "31 July 2013"
__version__ = "0.0.3"
__version_info__ = (0,0,3)
__license__ = "BSD"

from datetime import datetime, timedelta
import math

def first_of_day(date):
    return date.replace(hour=0, minute=0, second=0, microsecond=0)

def end_of_day(date):
    return date.replace(hour=23, minute=59, second=59, microsecond=999999)

def date_ranges(dt1, dt2):
    first = first_of_day(dt1)
    last = end_of_day(dt2)

    numdays = (last-first).days+1
    print numdays

    dateList = [ first + timedelta(days=x) for x in range(0,numdays) ]

    ranges = []
    for start in dateList:
        ranges.append((start, end_of_day(start)))

    return ranges    

def first_of_week(date):

    date = date.replace(hour=0, minute=0, second=0, microsecond=0)
    weekday = date.isoweekday()

    # If it's Sunday then we're done.
    if weekday == 7:
        return date

    return date - timedelta(days=weekday)

def end_of_week(date):
    return first_of_week(date) + timedelta(weeks=1, seconds=-1)

def week_ranges(dt1, dt2):
    first = first_of_week(dt1)
    last = end_of_week(dt2)

    numweeks = int(math.ceil((last-first).days/7.))

    dateList = [ first + timedelta(days=x*7) for x in range(0,numweeks) ]

    ranges = []
    for start in dateList:
        ranges.append((start, end_of_week(start)))

    return ranges

def first_of_month(date):
    return date.replace(day=1)

def end_of_month(date):
    if date.month == 12:
        return date.replace(day=31, hour=23, minute=59, second=59, microsecond=999999)
    
    return date.replace(month=date.month+1, day=1, hour=23, minute=59, second=59, microsecond=999999) - timedelta(days=1)

def month_ranges(dt1, dt2):

    start_month = dt1.month
    end_months=(dt2.year-dt1.year)*12 + dt2.month+1

    dates=[datetime(year=yr, month=mn, day=1) for (yr, mn) in (
        ((m - 1) / 12 + dt1.year, (m - 1) % 12 + 1) for m in range(start_month, end_months)
    )]

    ranges = []
    for start in dates:
        ranges.append((start, end_of_month(start)))

    return ranges

if __name__ == "__main__":
    for x in date_ranges(datetime.now(), datetime(2012, 6, 5, 4, 44, 12)):
        print x

    print "----"

    for x in week_ranges(datetime.now(), datetime(2012, 7, 13, 4, 44, 12)):
        print x

    print "----"

    for x in month_ranges(datetime(2012, 2, 13, 4, 44, 12), datetime(2013, 2, 13, 4, 44, 12)):
        print x

