"""
This is the main loop file for our AutoTube Bot!

Quick notes!
- Currently it's set to try and post a video then sleep for a day.
- You can change the size of the video currently it's set to post shorts.
    * Do this by adding a parameter of scale to the image_save function.
    * scale=(width,height)
"""

from datetime import date
import time
from utils.CreateMovie import CreateMovie, GetDaySuffix
from utils.RedditBot import RedditBot
from utils.upload_video import upload_video
import random


#Create Reddit Data Bot
redditbot = RedditBot()

# Leave if you want to run it 24/7
# while True:

    # Gets our new posts pass if image related subs. Default is memes
posts = redditbot.get_posts("discordVideos")

    # Create folder if it doesn't exist
# redditbot.create_data_folder()
num = 1
print("mainFlag")
# Go through posts and find 5 that will work for us.
for post in posts:
    redditbot.save_image(post)
    print(num,"main.py", post)
    num += 1

# Wanted a date in my titles so added this helper
DAY = date.today().strftime("%d")
DAY = str(int(DAY)) + GetDaySuffix(int(DAY))
dt_string = date.today().strftime("%A %B") + f" {DAY}"

# Create the movie itself!
CreateMovie.CreateMP4(redditbot.post_data)

# Video info for YouTube.
# This example uses the first post title.
titles = ["offensive memes if ylyl", "Offensive Memes I Stole From Discord", "Memes from 2093"]
video_data = {
        "file": "video.mp4",
        "title": f"{random.choice(titles)} v{random.randint(1, 100)}",
        "description": "#youtubememes #memes #meme\nDo comment if you own any of the clips\n\n\n",
        "keywords":"youtubememes,trynottolaugh,funny",
        "privacyStatus":"public"
}

# print(video_data["title"])
print(f"{random.choice(titles)} v{random.randint(1, 100)}")
print("Posting")
# time.sleep(60 * 60 * 24 - 1)
upload_video(video_data)

# Sleep until ready to post another video!

