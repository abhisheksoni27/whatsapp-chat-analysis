import re

##############################
# CLEAN TEXT
##############################

mediaPattern = r"(\<Media omitted\>)"
regexMedia = re.compile(mediaPattern, flags=re.M)

dateAndTimepattern = r"(\d+\/\d+\/\d+)(,)(\s)(\d+:\d+)(\s)(\w+)(\s)(-)(\s\w+)*(:)"
regexDate = re.compile(dateAndTimepattern, flags=re.M)

def cleanText(filename):    
    chat = open(filename)
    chatText = chat.read()

    # 01/09/17, 11:34 PM - Innaya:

    chatText = regexMedia.sub("", chatText)
    chatText = regexDate.sub("", chatText)

    lines = []

    for line in chatText.splitlines():
        if line.strip() is not "":
            lines.append(line.strip())

    return lines