# The Python documentation for the datetime module provides two attributes to retrieve the year from a date or datetime object: year and isocalendar.

# from datetime import date

# today = date.today()

# today_year = today.year
# iso_year = today.isocalendar()[0]

# What is the difference between the year attribute and the isocalendar method?

The year attribute gives a year between MINYEAR (the smallest year number allowed in a date or datetime object, i.e., 1) and MAXYEAR (the largest, i.e., 9999) inclusive.

The isocalendar method returns a named tuple object with year, week, and weekday.