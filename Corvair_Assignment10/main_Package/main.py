# File Name : main.py
# Student Name: Jacob Farrell
# email:  farrelcj@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   4/10/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:This assignment involved collaborating with a group to connect to and extract data from a third-party API. 
# We chose YouTube Data API to retrieve the top 10 trending videos in the US, process the returned data, and export the results to a CSV file.

# Brief Description of what this module does: This module is the entry point for our program. It executes our program
# and after retrieving the data, it prints to the console in a readable format, and then saves the data to a csv file.
# Citations: https://www.youtube.com/watch?v=q5uM4VKywbA - CSV assistance. https://www.youtube.com/watch?v=TE66McLMMEw - YouTube API assistance.


# Anything else that's relevant:

from api_Package.youtube_API import YouTubeTopVideos

def main():
    """
    Entry point for the YouTube trending video extractor.

    @param None
    @return None
    """
    yt = YouTubeTopVideos()
    data = yt.fetch_top_videos()
    videos = yt.parse_and_display(data)
    yt.save_to_csv(videos)


if __name__ == "__main__":
    main()

