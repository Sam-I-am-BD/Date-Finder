# Date Finder: Finds dates in the dd/mm/yyyy format
import re

dateRegex = re.compile(
    r"""
(3[0-9]|[1-2][0-9]|0?[1-9]) # search for day 1-31 and leading zeros
(/)                         # search for /
(1[0-2]|0?[1-9])           # search for month 1 - 12
(/)                         # search for /
([1-2][0-9][0-9][0-9])      # search for year 1000 - 2999
""",
    re.VERBOSE,
)
mo = dateRegex.findall("31/12/1999 01/01/2000 01/04/2000 31/04/2000 28/2/2000")
leadingZero = ('01', '02', '03', '04', '05', '06', '07', '08', '09')
days30 = ['4', '6', '9', '11']
days28 = '2'
days31 = ['1', '3', '5', '7', '8', '10', '12']
for i in range(len(mo)):
    day, slash1, month, slash2, year = mo[i]
    if day in leadingZero: #these two if statements remove leading zeros
        day = day[1]
    if month in leadingZero:
        month = month[1]
    if month in days31:
        if day < '32':
            print('The day ' + day + ' in the month ' + month + ' is valid.')
        else:
            print('The day: ' + day + ' in the month: ' + month + ' is NOT valid.')
    elif month in days30:
        if day < '31':
            print('The day ' + day + ' in the month ' + month + ' is valid.')
        else:
            print('The day: ' + day + ' in the month: ' + month + ' is NOT valid.')
    elif month == days28:
        if day < '29':
            print('The day ' + day + ' in the month ' + month + ' is valid.')
        else:
            print('The day: ' + day + ' in the month: ' + month + ' is NOT valid.')
    else:
        print('The day: ' + day + ' in the month: ' + month + ' is NOT valid.')


