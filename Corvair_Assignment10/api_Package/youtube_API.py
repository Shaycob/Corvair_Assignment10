# File Name : youtube_API.py
# Student Name: Matthew Boutros
# email:  boutromw@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   4/10/2025
# Course #/Section:   IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: # Brief Description of the assignment:This assignment involved collaborating with a group to connect to and extract data from a third-party API. 
# We chose YouTube Data API to retrieve the top 10 trending videos in the US, process the returned data, and export the results to a CSV file.
# Brief Description of what this module does: This module searches YouTube videos using the API, extracts key info, and saves the results to a CSV file.
# Citations: https://www.youtube.com/watch?v=q5uM4VKywbA - CSV assistance. https://www.youtube.com/watch?v=TE66McLMMEw - YouTube API assistance.

# Anything else that's relevant: N/A

import requests
import csv

class YouTubeTopVideos:
    def __init__(self):
        """
        Initialize the YouTubeTopVideos object with default API key, base URL, and region code.
        """
        self.api_key = "AIzaSyA-8gC_PnMkIUFQ7qszYvXOTyZ-soXaEf0" 
        self.base_url = "https://www.googleapis.com/youtube/v3/videos"
        self.region_code = "US"

    def fetch_top_videos(self, max_results=10):
        """
        Fetch the most popular YouTube videos using the YouTube Data API.

        @param max_results int: The maximum number of results to return (default = 10).
        @return dict: The JSON response from the API containing data.
        @raises HTTPError: If request to API fails.
        """
        params = {
            "part": "snippet,statistics",
            "chart": "mostPopular",
            "maxResults": max_results,
            "regionCode": self.region_code,
            "key": self.api_key
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json()

    def parse_and_display(self, data):
        """
        Parse video data from API response and print video details.

        @param data dict: The JSON data returned from the YouTube API.
        @return list: A list of video information, each as a list.
        """
        videos = []
        for item in data.get("items", []):
            title = item["snippet"]["title"]
            channel = item["snippet"]["channelTitle"]
            views = item["statistics"].get("viewCount", "N/A")
            likes = item["statistics"].get("likeCount", "N/A")
            print(f"Title: {title}\nChannel: {channel}\nViews: {views}\nLikes: {likes}\n")
            videos.append([title, channel, views, likes])
        return videos

    def save_to_csv(self, videos, filename="youtube_data.csv"):
        """
        Save parsed video data to a CSV file

        @param videos list: A list of lists containing video data (title, channel, views, likes)
        @param filename str: The name of the CSV file to save (default is 'youtube_data.csv')
        @return None
        """
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Channel", "Views", "Likes"])
            writer.writerows(videos)



