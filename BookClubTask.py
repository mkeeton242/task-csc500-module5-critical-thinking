###
# Project:      BookClubTask.py
# Author:       Michael Keeton
# Created:      10/13/2024
# Description:  Program that displays number of book clubs points.
###

def main():
    # Variable to store data in.
    num_books = int(input('Enter the number of books purchased this month: '))
    
    # Determine number of points earned.
    if num_books >= 8:
        num_points = 60
    elif num_books >= 6:
        num_points = 30
    elif num_books >= 4:
        num_points = 15
    elif num_books >= 2:
        num_points = 5
    else:
        num_points = 0
    
    print(f'{num_points:d} points earned this month.')
    
main()
