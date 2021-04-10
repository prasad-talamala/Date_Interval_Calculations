import datetime
from datetime import date


def is_saturday_and_multiple_of_five(d):
    year, month, day = d[:4], d[4:6], d[-2:]
    if 10 > int(month) > 0:
        month = month.strip("0")
    day_name = datetime.date(int(year), int(month), int(day)).strftime("%A")

    if int(d) % 5 == 0 and day_name == "Saturday":
        return True
    else:
        return False


def get_fourth_saturday(d):
    year, month, day = d[:4], d[4:6], d[-2:]
    if 10 > int(month) > 0:
        month = month.strip("0")
    if date(int(year), int(month), 1).strftime("%A") == "Sunday":
        fourth_saturday = 35 - date(int(year), int(month), 1).isoweekday()
    else:
        fourth_saturday = 28 - date(int(year), int(month), 1).isoweekday()
    if fourth_saturday == int(day):
        return True
    else:
        return False


def is_valid_date(d):
    isValidDate = True
    year, month, day = d[:4], d[4:6], d[-2:]

    if 10 > int(month) > 0:
        month = month.strip("0")
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False

    return isValidDate


def get_interval_dates(startdate, enddate):
    list_of_dates = []
    for d in range(startdate, enddate+1):
        if is_valid_date(str(d)):
            if get_fourth_saturday(str(d)) ^ is_saturday_and_multiple_of_five(str(d)):
                list_of_dates.append(str(d))

    return list_of_dates


a, b = 20210103, 20210303
output = get_interval_dates(a, b)
print("\n".join(output))
