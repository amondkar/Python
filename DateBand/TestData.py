def stageSalesData():
    salesPeriod = DateRange(date(2021, 1, 1), date(2021, 12, 31))
    priceDateBand1 = DateRange(date(2021, 1, 1), date(2021, 6, 30))
    priceDateBand2 = DateRange(date(2021, 7, 1), date(2021, 12, 31))
    discountsalesPeriod = DateRange(date(2021, 2, 1), date(2021, 3, 31))

    salesBands = []
    salesBands.append((salesPeriod, 'SP1'))
    salesBands.append((priceDateBand1, 'PB1'))
    salesBands.append((priceDateBand2, 'PB2'))
    salesBands.append((discountsalesPeriod, 'DS1'))

    return salesBands


def stageBookingData():
    bookingPeriod = DateRange(date(2020, 12, 1), date(2021, 11, 30))
    discountbookingPeriod = DateRange(date(2021, 1, 1), date(2021, 2, 28))

    bookingBands = []
    bookingBands.append((bookingPeriod, 'BP1'))
    bookingBands.append((discountbookingPeriod, 'DS1'))

    return bookingBands
