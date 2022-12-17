#scan
# Set the YouTube API key
API_KEY = "AIzaSyBuSPwBsCCbDPc1vgKJbhaU03wkGI-6fmQ"

# Authenticate and create a service object
service = build("youtube", "v3", developerKey=API_KEY)

# Set the video ID for which you want to get the comments
video_id = "gkwpe-CldJo"

# Set the maximum number of comments to return
max_results = 100

try:
    # Call the YouTube API to get the comments for the specified video
    response = service.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results,
        textFormat="plainText"
    ).execute()

    # Loop through the comments and print them
    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]
        author = comment["snippet"]["authorDisplayName"]
        text = comment["snippet"]["textDisplay"]
        print(f"Comment by {author}: {text}")

except HttpError as error:
    print(f"An error occurred: {error}")
