#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import os

'''
This function makes commit for given number of days
@inNumberOfDays: number of days for which we want to
				 make commit in past
'''
def HackForDays(inNumberOfDays):

	print('===='*19)

	#Iterate the given number of days
	for itr in range(inNumberOfDays):

		'''
		Update it at every iteration to
		make each commit unique
		'''
		dateString = str(itr) + ' day ago \n'
		
		'''
		Open log file and write commit date string.
		This is done because for every new commit we
		need to have some chagnes. Hence the @datString
		will always change. 
		'''
		with open('commit.log', 'w') as logFile:
			logFile.write(dateString)

		'''
		Add the changes and make a commit
		git commit --date is used to make commit in past
		'''
		os.system('git add .')
		os.system('git commit --date="' + dateString + '" -m "commit via HackChart script"')


	#Finally push all the commits to the github
	os.system('git push -u')

	print('===='*19)

	#Print success message
	successString = "\nI have successfully hacked your github contribution chart📈 for last " + str(inNumberOfDays)

	if inNumberOfDays == 1:
		dayType = " day🥳"
	else:
		dayType = " days🥳"

	print(successString+dayType)

	return True


'''
This function checks whether given input is of integer
type or not
@inNumberOfDays: number of days for which we want to
				 make commit in past
'''
def CheckInputType(inNumberOfDays):
	
	try:
		daysAsInt = int(inNumberOfDays)
		return daysAsInt

	except:
		print("\nI caught you trying to hack me🙂 \nI expect only integer input")
		return 0


'''
Program entry point
'''
if __name__ == "__main__":

	helpString = "\n\n\t📈HACK GITHUB CONTRIBUTION CHART📈 \n"\
	"\nEnter number of days for which you want to make commit in past\n"\
	"Format: Number of Days in integer format\n"\
	"Example: 107 (if you want to make commit for last 107 days)\n"\
	"\nYour Input: "

	numberOfDays = input(helpString)
	numberOfDays = CheckInputType(numberOfDays)

	if numberOfDays > 0:
		HackForDays(numberOfDays)

	print("\nGOODBYE👋\n")
				