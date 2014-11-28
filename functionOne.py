def calcWeeklyWages(totalHours,hourlyWage):
	if(totalHours<40):
		totalWage=totalHours*hourlyWage
	else:
		overtime=totalHours-40
		totalWage=totalHours*hourlyWage+(1.5*hourlyWage)*overtime
	return totalWage

def main():
	hours=float(input('Enter Hours '))
	wage=float(input('Enter hourly pay '))
	total=calcWeeklyWages(hours,wage)
	print('Wages for {hours} at wage ${wage} per hour is ${total}'.format(**locals()))

main()
