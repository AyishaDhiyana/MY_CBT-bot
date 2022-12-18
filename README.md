# CYBER BULLYING DETECTION
Our project is cyberbullying detection ,it is mainly aimed at scanning the comments under a youtube video and filtering out the hate comments and finally deleting those annoying comments.This code is using the YouTube API to get a list of comments for a specified video, and then filtering out any comments that contain certain words (specified in the exclude_words list) using Python's re module. The comments that pass the filter are added to the filtered_comments list and then printed.

The YouTube API is a service that allows developers to access YouTube data and functionality through an API. In this case, the code is using the commentThreads().list() method of the YouTube API to get the top-level comments for a given video. The maxResults parameter specifies the maximum number of comments to return, and the textFormat parameter specifies the format in which the comments should be returned (in this case, plain text).

The HttpError exception is caught in case there is an error when calling the API.

The re module is used to delete any instances of the words in the exclude_words list from the comments using regular expressions.if any words in the comments  matches any of the words specified in the exclude_words list , The re.sub() function is then used to replace these matches with an empty string. The filtered comments are added to the filtered_comments list, and then the list is printed.
