# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'netflix_ratings.csv')

movie = input("Please enter the movie you are looking for:")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read each row of data after the header
    for row in csvreader:
        if row[0] == movie:
            print()

