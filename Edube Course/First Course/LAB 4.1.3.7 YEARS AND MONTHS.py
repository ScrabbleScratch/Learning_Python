#Function to test if a year is leap
def isYearLeap(year):
    
    #To return the Fabruary days
    if year % 4 != 0:
        return 28
    elif year % 100 != 0:
        return 29
    elif year % 400 != 0:
        return 28
    else:
        return 29

    #To return True or False
    
    #if year % 4 != 0:
    #    return False
    #elif year % 100 != 0:
    #    return True
    #elif year % 400 != 0:
    #    return False
    #else:
    #    return True

#Function to determine how many days has a year month
def daysInMonth(year, month):
    months = [31, isYearLeap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return months[month-1]

#Test data
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]

#To test every Test data
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
