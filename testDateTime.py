import datetime

# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))

''' 
Creating Date Objects To create a date, we can use the datetime() class 
(constructor) of the datetime module.
The datetime() class requires three parameters to create a date: year, month
, day.

'''

# x = datetime.datetime(2020, 5, 17)
# print(x)

'''
the datetime() class also takes parameters for time and timezone ()
(hour, minute, second, microsecond, tzone), but they are optional, 
and has default value of 0, (None for timezone).
'''

'''
The strftime() MethodtttttttttttttttExtensionstttttttttt
The datetime object has method for formatting date objects into readable
strings. The method is call strftime(), and take one parameter, format, 
to specify the format of the returned string:

Example
Display the name of the month:

'''

# x = datetime.datetime(2018, 6, 1)
# print(x.strftime("%B"))

x = datetime.datetime.now()

# short weekday
# print(x.strftime("%a")) 

# weekday full version
# print(x.strftime("%A"))

# weekday as a number 0-6 0 is Sunday