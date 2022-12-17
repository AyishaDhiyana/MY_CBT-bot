import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import re

# Set the YouTube API key
API_KEY = "AIzaSyBuSPwBsCCbDPc1vgKJbhaU03wkGI-6fmQ"

# Authenticate and create a service object
service = build("youtube", "v3", developerKey=API_KEY)

# Set the video ID for which you want to get the comments
video_id = "gkwpe-CldJo"

# Set the maximum number of comments to return
max_Results = 100

try:
    # Call the YouTube API to get the comments for the specified video
    response = service.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_Results,
        textFormat="plainText"
    ).execute()

    # Loop through the comments and print them
    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]
        author = comment["snippet"]["authorDisplayName"]
        text = comment["snippet"]["textDisplay"]
        # print(f"Comment by {author}: {text}")

except HttpError as error:
    print(f"An error occurred: {error}")



# define a list of words to exclude
exclude_words = ['Cumbubble','F*ck','shit','Get Lost','F*ck you','Shitbag','Piss off','Asshole','Dickweed','C*nt','Son of a bitch','F*ck trumpet','Bastard','Bitch','Bollocks','Bugger''Cocknose','Bloody hell','Knobhead''Choad','Bitchtits','Crikey','Rubbish','Pissflaps','Shag','Wanker','Talking the piss','Twat','Arsebadger','Jizzcock','Cumdumpster','Shitmagnet','Scrote','Twatwaffle','Thundercunt','Dickhead','Shitpouch','Jizzstain','Nonce','Pisskidney','Wazzock','Cumwipe','Fanny','Bellend','Pisswizard','Knobjockey','Cuntpuddle','Dickweasel','Quim','Bawbag','Fuckwit','Tosspot','Cockwomble','Twat face','Cack','Flange','Clunge','Dickfucker','Fannyflaps','Wankface','Shithouse','Gobshite','Jizzbreath','Todger','Nutsack','Dick','shit']
filtered_comments=[]

for item in response ["items"]:
   # get the comment text and author name

   text = item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
   author = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
   # check if any of the exclude words are in the sentence
   if not any(word in text for word in exclude_words):
     # print the comment with the author name
     print(f"Comment by {author}: {text}")
