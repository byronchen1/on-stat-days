import datetime as dt


easter2000_2099 = [
                    '2020-04-10',
                    '2021-04-02',
                    '2022-04-15',
                    '2023-04-07',
                    '2024-03-29',
                    '2025-04-18',
                    '2026-04-03',
                    '2027-03-26',
                    '2028-04-14',
                    '2029-03-30',
                    '2030-04-19',
                    '2031-04-11',
                    '2032-03-26',
                    '2033-04-15',
                    '2034-04-07',
                    '2035-03-23',
                    '2036-04-11',
                    '2037-04-03',
                    '2038-04-23',
                    '2039-04-08',
                    '2040-03-30',
                    '2041-04-19',
                    '2042-04-04',
                    '2043-03-27',
                    '2044-04-15',
                    '2045-04-07',
                    '2046-03-23',
                    '2047-04-12',
                    '2048-04-03',
                    '2049-04-16',
                    '2050-04-08',
                    '2051-03-31',
                    '2052-04-19',
                    '2053-04-04',
                    '2054-03-27',
                    '2055-04-16',
                    '2056-03-31',
                    '2057-04-20',
                    '2058-04-12',
                    '2059-03-28',
                    '2060-04-16',
                    '2061-04-08',
                    '2062-03-24',
                    '2063-04-13',
                    '2064-04-04',
                    '2065-03-27',
                    '2066-04-09',
                    '2067-04-01',
                    '2068-04-20',
                    '2069-04-12',
                    '2070-03-28',
                    '2071-04-17',
                    '2072-04-08',
                    '2073-03-24',
                    '2074-04-13',
                    '2075-04-05',
                    '2076-04-17',
                    '2077-04-09',
                    '2078-04-01',
                    '2079-04-21',
                    '2080-04-05',
                    '2081-03-28',
                    '2082-04-17',
                    '2083-04-02',
                    '2084-03-24',
                    '2085-04-13',
                    '2086-03-29',
                    '2087-04-18',
                    '2088-04-09',
                    '2089-04-01',
                    '2090-04-14',
                    '2091-04-06',
                    '2092-03-28',
                    '2093-04-10',
                    '2094-04-02',
                    '2095-04-22',
                    '2096-04-13',
                    '2097-03-29',
                    '2098-04-18',
                    '2099-04-10'
                    ]

stat_days = []
for i in range(2020, 2100):
    # New Year's Day = January 1
    stat_days.append(str(dt.date(i, 1, 1)))

    # Family Day = Third Monday in February = Feb 15 - 21
    for j in range(15, 22):
        if dt.date(i, 2, j).strftime("%A") == "Monday":
            stat_days.append(str(dt.date(i, 2, j)))
            break

    # Good Friday = Friday before Easter Sunday
    stat_days.append(easter2000_2099[i-2020])

    # Victoria Day = Monday before May 25 = May 18 - 24
    for j in range(18, 25):
        if dt.date(i, 5, j).strftime("%A") == "Monday":
            stat_days.append(str(dt.date(i, 5, j)))
            break

    # Canada Day = July 1
    stat_days.append(str(dt.date(i, 7, 1)))

    # Civic Holiday = First Monday in August = August 1 - 7
    for j in range(1, 8):
        if dt.date(i, 8, j).strftime("%A") == "Monday":
            stat_days.append(str(dt.date(i, 8, j)))
            break

    # Labour Day = First Monday in September = September 1 - 7
    for j in range(1, 8):
        if dt.date(i, 9, j).strftime("%A") == "Monday":
            stat_days.append(str(dt.date(i, 9, j)))
            break

    # Thanksgiving = Second Monday in October = October 8 - 14
    for j in range(8, 15):
        if dt.date(i, 10, j).strftime("%A") == "Monday":
            stat_days.append(str(dt.date(i, 10, j)))
            break

    # Christmas Day = December 25
    stat_days.append(str(dt.date(i, 12, 25)))

    # Boxing Day = December 26
    stat_days.append(str(dt.date(i, 12, 26)))

for k in stat_days:
    print(k)
