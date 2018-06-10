import re
import matplotlib.pyplot as plt
import numpy as np
import indicoio

indicoio.config.api_key = '26837191c44dd6a7560a688e3307920d'


def cleanText(filename, ownerName="Abhishek Soni"):

    chat = open(filename)
    personName = filename.split('.')[0]
    chatText = chat.read()
    pattern = "(\d+\/\d+\/\d+)(,)(\s)(\d+:\d+)(\s)(\w+)(\s)(-)(\s)(\w+)(\s\w+)?(:)"

    regex = re.compile(pattern, flags=re.M)

    clean = regex.sub("", chatText)
    lines = []
    for line in clean.splitlines():
        lines.append(line.strip())

    return lines


linesList =cleanText('innaya.txt')