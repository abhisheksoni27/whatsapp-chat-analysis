import re
import sys
import datetime
import matplotlib.pyplot as plt
from tqdm import tqdm


def split_text(filename):
    """
    Split file contents by newline.
    """
    chat = open(filename, encoding="utf8")
    chatText = chat.read()
    return chatText.splitlines()


def groupByHour(AM, PM):
    # Now group time into 1-hour intervals
    time_groups = {}

    for i in range(24):
        time_groups[str(i)] = 0  # skeleton container

    # if the hour is in AM
    for time in AM:
        # Since we are sorting by hours, we need not care about the minute information.
        current_hour = int(time.split(":")[0])

        if current_hour == 12:
            current_hour = 0  # Because we represent 12AM as 0 in our container

        current_hour = str(current_hour)
        time_groups[current_hour] += 1

    # Similarly for PM
    for time in PM:
        current_hour = int(time.split(":")[0])

        # Trick to map 12 PM to the correct key
        if current_hour == 24:
            current_hour = 12

        current_hour = str(current_hour)
        time_groups[current_hour] += 1

    return time_groups


def distributeByAmPm(linesText):
    timeRegex = re.compile("\d+\/\d+\/\d+, (\d+\:\d+)")

    AM, PM = [], []
    for index, line in tqdm(enumerate(linesText)):
#         print(index)
        matches = re.findall(timeRegex, line)
        if (len(matches) > 0):
            match = datetime.datetime.strptime(
                matches[0], "%H:%M").strftime('%p')

            if match == "AM":
                AM.append(matches[0])
            else:
                PM.append(matches[0])

    return AM, PM


def plot_graph(time_groups, name):
    plt.bar(range(len(time_groups)), list(
        time_groups.values()), align='center')

    plt.xticks(range(len(time_groups)), list(time_groups.keys()))

    plt.xlabel('Time groups with 1 hour interval')
    plt.ylabel('Frequency')
    plt.title("Timing Analysis - Chat with {0}".format(name.capitalize()))
    plt.grid(1)
    plt.show()


def analyze(name):
    linesText = split_text(name)

    # Distribute into AM and PM
    AM, PM = distributeByAmPm(linesText)

    # Now group time into 1-hour intervals
    time_groups = groupByHour(AM, PM)

    # Plot
    plot_graph(time_groups, name)


analyze(sys.argv[1])
