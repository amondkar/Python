from datetime import date, datetime, timedelta
from DateRange import DateRange
import operator
from copy import copy


def splitDateRange(dateRangeList, newDateRange):

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
            return [DateRange(dates[0], dates[1]-oneday), DateRange(dates[1], dates[2])]
        else:
            return [DateRange(dates[0], dates[1]), DateRange(dates[1]+oneday, dates[2])]

    else:
        return [DateRange(dates[0], dates[1]-oneday), DateRange(dates[1], dates[2]), DateRange(dates[2]+oneday, dates[3])]


def stageSalesData():
    salesPeriod = DateRange(date(2021, 1, 1), date(2021, 12, 31))
    priceDateBand1 = DateRange(date(2021, 1, 1), date(2021, 12, 31))
    sup1 = DateRange(date(2021, 3, 1), date(2021, 6, 30))
    sup2 = DateRange(date(2021, 3, 1), date(2021, 6, 30))
    discountsalesPeriod1 = DateRange(date(2021, 3, 1), date(2021, 4, 30))
    discountsalesPeriod2 = DateRange(date(2021, 4, 1), date(2021, 5, 31))

    salesBands = []
    salesBands.append((salesPeriod, 'SP1'))
    salesBands.append((priceDateBand1, 'PB1'))
    salesBands.append((sup1, 'SUP1'))
    salesBands.append((sup1, 'SUP2'))
    salesBands.append((discountsalesPeriod1, 'DS1'))
    salesBands.append((discountsalesPeriod2, 'DS2'))

    return salesBands


def stageBookingData():
    bookingPeriod = DateRange(date(2020, 12, 1), date(2021, 11, 30))
    discountbookingPeriod1 = DateRange(date(2021, 2, 1), date(2021, 3, 31))
    discountbookingPeriod2 = DateRange(date(2021, 3, 1), date(2021, 4, 30))

    bookingBands = []
    bookingBands.append((bookingPeriod, 'BP1'))
    bookingBands.append((discountbookingPeriod1, 'DS1'))
    bookingBands.append((discountbookingPeriod2, 'DS2'))

    return bookingBands


def generateDateRange(dateBands):
    dateRanges = []

    for dateBand, key in dateBands:
        if(len(dateRanges) == 0):
            dateRanges.append(dateBand)
        else:
            dateRanges = splitDateRange(dateRanges, dateBand)

    return dateRanges


def test():

    salesPeriod = DateRange(date(2021, 1, 1), date(2021, 12, 31))
    priceDateBand1 = DateRange(date(2021, 1, 1), date(2021, 6, 30))
    priceDateBand2 = DateRange(date(2021, 7, 1), date(2021, 12, 31))

    dateBandList = []
    dateBandList.append(salesPeriod)
    dateBandList = generateDateRange(dateBandList, priceDateBand1)

    print(dateBandList)

    dateBandList = generateDateRange(dateBandList, priceDateBand2)

    print(dateBandList)

    dateBandList = generateDateRange(
        dateBandList, DateRange(date(2021, 5, 1), date(2021, 8, 31)))

    print((dateBandList))

    print(sorted(set(dateBandList), key=lambda x: x.start_dt))


def populateKeys(dateBands, dateRanges):
    dateRangeKeys = []

    for dateRange in dateRanges:
        keys = set()
        for dateBand, key in dateBands:

            if(operator.contains(dateBand, dateRange)):
                keys.add(key)
        dateRangeKeys.append((dateRange, keys))
    return dateRangeKeys


def populatePairs(salesDateRangeWithKeys, bookingDateRangeWithKeys):
    dateRangePairs = []
    for salesDateRange, salesKeys in salesDateRangeWithKeys:
        bookingDateRanges = []
        for bookingDateRange, bookingKeys in bookingDateRangeWithKeys:
            if(bookingDateRange.start_dt <= salesDateRange.end_dt):
                bookingDateRanges.append(
                    (adjustBookingEndDt(bookingDateRange, salesDateRange), adjustKeys( salesKeys,bookingKeys)))
        dateRangePairs.append(((salesDateRange, salesKeys), bookingDateRanges))
    return dateRangePairs


def adjustBookingEndDt(bookingDateRange, salesDateRange):
    bookingDateCopy = copy(bookingDateRange)
    if(bookingDateCopy.end_dt > salesDateRange.end_dt):
        bookingDateCopy.end_dt = salesDateRange.end_dt
    return bookingDateCopy


def adjustKeys(salesKeys, bookingKeys):
    return (salesKeys & bookingKeys)


def findPairs(salesDateBands, bookingDateBands):
    salesDateRanges = set(generateDateRange(salesDateBands))
    bookingDateRanges = set(generateDateRange(bookingDateBands))

    print('Sales Date Range: {!r}'.format(salesDateRanges))
    print('Booking Date Range: {!r}'.format(bookingDateRanges))

    salesDateRangeWithKeys = populateKeys(salesDateBands, salesDateRanges)
    print('Sales Date Range With Keys: {!r}'.format(salesDateRangeWithKeys))

    bookingDateRangeWithKeys = populateKeys(
        bookingDateBands, bookingDateRanges)
    print('Booking Date Range With Keys: {!r}'.format(
        bookingDateRangeWithKeys))

    pairs = populatePairs(salesDateRangeWithKeys, bookingDateRangeWithKeys)

    printPairs(pairs)

def printPairs(pairs):
    
    for salesDateWithKeys, bookingDates in pairs:
        salesDate, salesKeys = salesDateWithKeys
        print('Sales Dates: {} - {}'.format(salesDate.start_dt.strftime('%Y-%m-%d'),salesDate.end_dt.strftime('%Y-%m-%d')))
        print('Sales keys: {} '.format(salesKeys))

        for bookingDate, bookingKey in bookingDates:
            print('         Booking Dates: {} - {}'.format(bookingDate.start_dt.strftime('%Y-%m-%d'),bookingDate.end_dt.strftime('%Y-%m-%d')))
            print('         Booking keys: {} '.format(bookingKey))
findPairs(stageSalesData(), stageBookingData())

x = {2, 3, 5, 6}
y = {1, 2, 3, 4}

x.add(1)

z = x ^ y

print(z)
