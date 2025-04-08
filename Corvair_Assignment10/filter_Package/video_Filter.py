# File Name : video_filter.py
# Student Name: Daquan Daniels 
# email:  danieldu@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   04/10/25
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025 
# Brief Description of the assignment:# Brief Description of the assignment:This assignment involved collaborating with a group to connect to and extract data from a third-party API. 
# We chose YouTube Data API to retrieve the top 10 trending videos in the US, process the returned data, and export the results to a CSV file. 

# Brief Description of what this module does: Reads video data, checks view count, filters qualifying videos, and writes them to a new CSV file.
# Citations: N/A

# Anything else that's relevant: N/A
import csv

def filter_by_views(min_views=1000000, in_file="youtube_data.csv", out_file="filtered_videos.csv"):
    """
    Filter YouTube videos by minimum views and write results to a new CSV file.

    @param min_views int: The minimum number of views a video must have to be included
    @param in_file String: The input CSV file containing video data
    @param out_file String: The output CSV file to save filtered results
    @return None
    """
    with open(in_file, newline='', encoding="utf-8") as infile, \
         open(out_file, mode="w", newline='', encoding="utf-8") as outfile:


        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        print(f"Videos with more than {min_views} views:")
        for row in reader:
            try:
                views = int(row["Views"])
                if views > min_views:
                    writer.writerow(row)
                    print(f"{row['Title'][:50]:<50} | Views: {views}")
            except ValueError:
                continue

if __name__ == "__main__":
    filter_by_views(min_views=1000000)


