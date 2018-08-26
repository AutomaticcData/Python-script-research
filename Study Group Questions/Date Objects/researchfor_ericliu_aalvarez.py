# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 20:43:09 2018

@author: anthonyalvarez
"""


import datetime
import calendar


#--------------------  ERIC LIU - UCI ------------------------------
#QUESTION: Anyone has idea how to find the third day from the last day of a month?
#For example: Aug 29 for Aug
#
#AALVAREZ - Research -----------------------------------------
#Part 1, provided that the date is in a usable date format
#for this i am assuming that it isnt, so i researched date conversions
#from the Stack example referenced below
#https://stackoverflow.com/questions/466345/converting-string-into-datetime
#response 811
#-------------------------------------------------------------------
date_str = '29/12/2017' # The date - 29 Dec 2017
format_str = '%d/%m/%Y' # The format
datetime_obj = datetime.datetime.strptime(date_str, format_str)
#print(datetime_obj.date())
#--------------------------------------------------------------------

#===== testing string conversions =======
#mydate = datetime_obj.date()
#print(f'My Date: {mydate}')

#myyear = mydate.year
#print(myyear)

#mymonth = mydate.month
#print(mymonth)

#myday = mydate.day
#print(myday)


#===== updating the date to use Erics example Aug 29 =========
#Assuming year is 2018 and month is 08 - AUGUST
#https://stackoverflow.com/questions/1133147/how-to-extract-the-year-from-a-python-datetime-object

#===== testing date parts =======
#print('calendar:')
#print(calendar.monthrange(2002,1))    #RETURNS THE RANGE OF THE MONTH >> (1, 31)
#print(calendar.monthrange(2002,1)[1]) #USING SLICING TO RETURN THE SECOND VALUE >> 31

erics_date = '2018-01-08'
print(f'Original string date: {erics_date}')

date_format = '%Y-%m-%d'
erics_date_obj = datetime.datetime.strptime(erics_date, date_format)

#values to pass to calendar object
emonth = erics_date_obj.month
eyear = erics_date_obj.year

#in this case we want the second value returned for the days
erics_lastdayofmonth = calendar.monthrange(eyear, emonth)[1]
print(f'The last day of the month for the year {eyear} is {erics_lastdayofmonth}')

#next we subtract 3 days or however many days you are looking for. Your example asks for "third day from the last day of a month"
requestedsearchdate = erics_lastdayofmonth - 3
print(f'The date we are looking for from the last day of the month is: {requestedsearchdate}')

#make a new valid date just in case its required
finalstringdate = str(eyear) + '-' + str(emonth) + '-' + str(requestedsearchdate)
print(f'The new string date is: {finalstringdate}')

final_date_obj  = datetime.datetime.strptime(finalstringdate, date_format)
print(f'The new date object is: {final_date_obj}')


