###
# Project:      RainfallTask.py
# Author:       Michael Keeton
# Created:      10/13/2024
# Description:  Program that displays total and average rainfall over a period.
###

def main():
    # Variables to store data in.
    rainfall_matrix = []
    rainfall_total = 0
    
    # List of months for prompt.
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    
    # Prompts the user for the number of years.
    num_years = int(input('Enter the number of years: '))
    
    # Iterate for each year.
    for i in range(num_years):
        rainfall_year = []
        print('YEAR', i + 1)
        # Iterate for each month.
        for j in range(12):
            inches_rain = float(input(f'Enter the inches of rainfall for {months[j]:s}: '))
            rainfall_total += inches_rain
            rainfall_year.append(inches_rain)
        rainfall_matrix.append(rainfall_year)
    
    # Print number of months, total rainfall, and average rainfall per month.
    total_num_months = num_years * 12
    print(f'Total Number of Months: {total_num_months:d}')
    print(f'Total Rainfall (inches): {rainfall_total:.2f}')
    print(f'Average Rainfall per Month (inches): {rainfall_total/total_num_months:.2f}')
    
    # Calculate and print average rainfall for each month.
    for i in range(12):
        rainfall_monthly = 0
        for j in range(num_years):
            rainfall_monthly += rainfall_matrix[j][i]
        print(f'Average Rainfall for {months[i]:s}: {rainfall_monthly/num_years:.2f}') 
main()
