# File Name : csv_reader.py
# Student Name: Omar Alkhawaga
# email:  alkhawoe@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:  4/10/2025
# Course #/Section:  IS4010/001
# Semester/Year:  Spring 2025
# Brief Description of the assignment:  # Brief Description of the assignment:This assignment involved collaborating with a group to connect to and extract data from a third-party API. 
# We chose YouTube Data API to retrieve the top 10 trending videos in the US, process the returned data, and export the results to a CSV file. 
# Brief Description of what this module does: This module reads data from the CSV file
# Citations: https://stackoverflow.com/questions/26903304/reading-data-from-a-csv-file-in-python
# Anything else that's relevant:N/A

import csv

def read_and_print_csv(filename="youtube_data.csv"):
    """
    Reads a CSV file containing YouTube video data and prints the content 

    Parameters: (str) The path to the CSV file. 'youtube_data.csv'.
    """
    with open(filename, newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)
        print(f"{headers[0]:<50} | {headers[1]:<20} | {headers[2]:>10} | {headers[3]:>10}")
        print("-" * 100)
        for row in reader:
            title, channel, views, likes = row
            print(f"{title[:50]:<50} | {channel:<20} | {views:>10} | {likes:>10}")

if __name__ == "__main__":
    read_and_print_csv()


