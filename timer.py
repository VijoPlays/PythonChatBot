import msvcrt
import time
import datetime

# In theory, this method takes the input of a user and then you can post it to the Twitters through the terminal.
# In practice this one never allows the bot to progress past this, so I'm just gonna give up on it
# (Though BackgroundScheduler may do what I want, too lazy for it now).
# Something more I would like this method to have: Backspace doesn't move to the left, but deletes instead.
# Enter *should* clear the comment string, but does not for whatever reason.


def readInput():
    start_time = time.time()
    comment = ""
    while True:
        while True:
            chrctr = msvcrt.getch().decode("utf-8")
            if str(chrctr) == '\n':
                return comment
            else:
                if str(chrctr) == "" and (time.time() - start_time) >= 4 and comment == "":
                    return
                comment += str(chrctr)
            break


timeOut = {
    "startUp": time.time(),
    "receivedQuoteTimer": "0"
}


def convertToTime(timeInSeconds):
    return str(datetime.timedelta(seconds=int(timeInSeconds)))

