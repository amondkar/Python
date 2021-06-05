from datetime import date, datetime, timedelta
import operator


class DateRangeKey:
    def __init__(self, start_dt, end_dt):
        self.start_dt = start_dt
        self.end_dt = end_dt
        #self.keys = keys

    def __eq__(self, other):
        return ((self.start_dt == other.start_dt) and (self.end_dt == other.end_dt))

    def contains(self, dt):
        return (self.start_dt <= dt <= self.end_dt)

    def __repr__(self):
        return '<DateRangeKey({!r}, {!r}>'.format(
            self.start_dt, self.end_dt
        )
    def __hash__(self):
      return hash((self.start_dt, self.end_dt))


def generateDateRange(dateRangeList, newDateRange):

    updateDateRangeList = []

    for dateRage in dateRangeList:
        if(((dateRage.contains(newDateRange.start_dt)) or (dateRage.contains(newDateRange.end_dt)))):
            updateDateRangeList.extend(adjustDateRange(dateRage, newDateRange))
        else:
            updateDateRangeList.append(dateRage)

    return updateDateRangeList


def adjustDateRange(dateRage, newDateRange):
    dates = sorted({
        dateRage.start_dt,
        dateRage.end_dt,
        newDateRange.start_dt,
        newDateRange.end_dt
    })

    oneday = timedelta(days=1)

    print(len(dates))


    if(dateRage.__eq__(newDateRange)):
        return [dateRage]
    elif(len(dates) == 3):
        adjustedDate = dates[1]+oneday
        if(newDateRange.contains(adjustedDate)):
            return [DateRangeKey(dates[0], dates[1]-oneday), DateRangeKey(dates[1], dates[2])]
        else:
            return [DateRangeKey(dates[0], dates[1]), DateRangeKey(dates[1]+oneday, dates[2])]
        
    else:
        return [DateRangeKey(dates[0], dates[1]-oneday),DateRangeKey(dates[1], dates[2]), DateRangeKey(dates[2]+oneday, dates[3])]


salesPeriod = DateRangeKey(date(2021, 1, 1), date(2021, 12, 31))
priceDateBand1 = DateRangeKey(date(2021, 1, 1), date(2021, 6, 30))
priceDateBand2 = DateRangeKey(date(2021, 7, 1), date(2021, 12, 31))

dateBandList = []
dateBandList.append(salesPeriod)
dateBandList = generateDateRange(dateBandList, priceDateBand1)

print(dateBandList)

dateBandList = generateDateRange(dateBandList, priceDateBand2)

print(dateBandList)

dateBandList = generateDateRange(
    dateBandList, DateRangeKey(date(2021, 5, 1), date(2021, 8, 31)))

print((dateBandList))

print(sorted(set(dateBandList), key=lambda x: x.start_dt))
