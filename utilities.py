import re

##############################
# CLEAN TEXT
##############################

def clean(self, filename):    
    chat = open(filename)
    chatText = chat.read()

    # 01/09/17, 11:34 PM - Innaya:

    mediaPattern = "(\<Media omitted\>)"
    regexMedia = re.compile(mediaPattern, flags=re.M)
    chatText = regexMedia.sub("", chatText)

    dateAndTimepattern = "(\d+\/\d+\/\d+)(,)(\s)(\d+:\d+)(\s)(\w+)(\s)(-)(\s\w+)*(:)"
    regexDate = re.compile(dateAndTimepattern, flags=re.M)
    chatText = regexDate.sub("", chatText)

    lines = []

    for line in chatText.splitlines():
        if line.strip() is not "":
            lines.append(line.strip())

    return lines