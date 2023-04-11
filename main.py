import datetime
from datetime import datetime, timedelta, date
"""ex.1 Write a function that calculates difference in days between two datetimes. """

# first_date = datetime.datetime(1990, 3, 11)
# second_date = datetime.datetime(1991, 3, 11)
# difference_in_days = second_date - first_date
# print(difference_in_days.days)


"""ex.2 Write a function that takes a datetime object, which will represent employees starting work day. and will return amount of total holidays gained during the work until today. 1 Month = 1.6 day off"""

# starting_date = datetime.datetime(2023, 1, 1)
# now = datetime.datetime.now()
# holiday_in_month = 1.6

# difference_in_month = now.month - starting_date.month
# holidays = round(difference_in_month * holiday_in_month, 2)
# print(holidays)

"""ex.3 find next 3 Fridays that happend to be Friday the 13th (classic)"""


# def get_upcoming_friday_13ths(start_date: datetime, count: int):
#     friday_13ths = []
#     while len(friday_13ths) < count:
#         start_date += timedelta(days=1)
#         if start_date.day == 13 and start_date.weekday() == 4:
#             friday_13ths.append(start_date)
#     return friday_13ths


# start_date = datetime.now()
# friday_13ths = get_upcoming_friday_13ths(start_date, 3)
# for date in friday_13ths:
#     print(date.strftime("%Y-%m-%d"))


"""ex4. Write a python function that takes nothing but returns the datetime object of last Friday"""

# today = date.today()
# days_in_week = 7
# next_friday = (today.weekday() - 4)
# last_friday = today - timedelta(days=next_friday + days_in_week)
# print(last_friday)


"""ex5.Write a Python program to get the last day of a specified year and month, Example: Monday, Tuesday etc."""


# def last_day_of_month(year:datetime, month:datetime):
#     last_day = date(year, month + 1, 1) - timedelta(days=1)
#     return last_day.strftime('%A')


# year = int(input("Enter year: "))
# month = int(input("Enter month: "))

# last_day = last_day_of_month(year, month)
# print(f"The last day of {year}/{month} is {last_day}.")

"""ex6. Write a terminal program that required user to login. If user does not have an account he should register. credentials are username and password. Store the information in the file txt or pickle. Validate user credentials from the file. Once user has logged in: print text: "Hello, <username>". """
