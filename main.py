import socket
import os
import random
from apscheduler.schedulers.background import BackgroundScheduler

import channelCommands
import timer

# Change nick to the channel you want to invade with the bot, change pass to the Oauth of your bot account.
address = "irc.twitch.tv"
port = 6667
channel = "vijoplays"                           # TODO: The channel you want to invade here.
auth = ""   # TODO: The auth token of your bot account here.

s = socket.socket()
s.connect((address, port))
s.send(bytes("PASS " + auth + "\r\n", "UTF-8"))
s.send(bytes("NICK " + channel + "\r\n", "UTF-8"))
s.send(bytes("JOIN #" + channel + " \r\n", "UTF-8"))

# Adjust these variables to adjust when a command is available again, in seconds.
cooldown = 300
cooldownSave = cooldown
quoteCooldown = 30
diceCooldown = 4
highlightCooldown = 120
quoteTimeout = 1200
quoteMessageRequirement = 20
giveawayTime = 15

# Don't.
giveawayActive = False
diceThrow = "diceThrow"
isBlacklisted = False
oldSong = ""


def schedule_routine(sender):
    """
This method checks which command is called (e.g. 'request' for any request commands) and then executes the specific code accordingly.
This method contains most of the intelligence, the rest is *mostly* just setup and preventing bugs.
    """
    try:
        if sender == "song":
            if message == "!song":
                curSong()
                timer.timeOut[username + message.lower()] = str(timer.time.time())
            elif message == "!rate":
                #TODO Old bot used to have a rating system, where every person could rate a song by entering !rate and a number between 1 and 7 (e.g. !rate 5)
                timer.timeOut[username + message.lower()] = str(timer.time.time())
            elif message == "!rating":
                # TODO Same - this as well as the normal song would display how often it was played and what the overall rating of the song was.
                timer.timeOut[username + message.lower()] = str(timer.time.time())

        elif sender == "request":
            if messageNoSpace == "!schedule":
                pathSchedule = open(channelCommands.pathSchedule, "r")
                send_message(str(channelCommands.pathCommands.get(channelPathKeys[i])) + pathSchedule.read())
                pathSchedule.close()

            elif messageNoSpace == "!song" or messageNoSpace == "!game" or messageNoSpace == "!command":
                send_message(channelCommands.pathCommands.get(channelPathKeys[i]))
                pathReq = open(channelCommands.pathRequest, "a")
                pathReq.write("\n" + channelPathKeys[i] + ": " + messageNoRequest)
                pathReq.close()

            elif messageNoSpace == "!shoutout" or messageNoSpace == "!so":
                send_message(str("Oh, hey guys! You should totally check out " + messageNoRequest + " over at https://www.twitch.tv/" + messageNoRequest + " ! This puny human probably creates nice content, or not. As a bot I don't have any feelings on either side regarding this."))

            else:
                send_message(random_line(str(channelCommands.pathCommands.get(channelPathKeys[i]))))
            timer.timeOut[username + message.lower()] = str(timer.time.time())

        elif sender == "uptime":
            send_message("I've been online for: " + (timer.convertToTime(timer.time.time() - bootingTime)) + ".")
            timer.timeOut[username + message.lower()] = str(timer.time.time())

        elif sender == "hahakeys":
            if message == "!donate":
                send_message("There doesn't seem to be anything here, " + username + "... Sorry! As of now, Vijo doesn't want to be a sellout.")
            else:
                send_message(str(channelCommands.hahaLinks.get(channelHahaKeys[i])))
            timer.timeOut[username + message.lower()] = str(timer.time.time())

        elif sender == "channelCommands":
            send_message("Here is the requested " + str(channelComKeys[i]).replace("!", "").capitalize() + " link, " + username + ": " + str(channelCommands.channels.get(channelComKeys[i])) + " !")
            timer.timeOut[username + message.lower()] = str(timer.time.time())

        elif sender == "giveaway":
            global giveawayActive

            if message == "!giveaway" and username.lower() == channel and giveawayActive is False:
                send_message("Giveaway is now starting, you have " + str(timer.convertToTime(giveawayTime)) + " hours time! Type !join to join.")
                giveawayActive = True
                channelCommands.giveaway["!timeleft"] = str(timer.time.time())

            if giveawayActive:
                timeLeft = float(
                    (float(giveawayTime) - float(timer.time.time()) + float(channelCommands.giveaway.get("!timeleft"))))
                if timeLeft <= 0:
                    if message == "!winner" and username.lower() == channel:
                        playerNum = channelCommands.giveawayPlayers.__len__() - 1
                        winner = random.randint(0, playerNum)
                        send_message("The winner is... " + list(channelCommands.giveawayPlayers.keys())[
                            winner] + "! Congratulations!!")

                else:
                    if message == "!cancelgiveaway" and username.lower() == channel:
                        send_message("The giveaway has been cancelled for... reasons! I'm sorry?")
                        giveawayActive = False
                        channelCommands.giveaway["!timeleft"] = ""

                    elif message == "!players":
                        send_message("We currently have " + str(
                            channelCommands.giveawayPlayers.__len__()) + " player(s) competing, still room for more!")

                    elif message == "!join":
                        send_message(username + " joined in on the fun, yey!")
                        channelCommands.giveawayPlayers[username] = ""

                    elif message == "!timeleft":
                        send_message("You still  have " + str(
                            timer.convertToTime(timeLeft)) + " hours left. Let's go, let's go!")

        elif sender == "dcp":
            if message == "!waste":
                send_message(username + str(channelCommands.dcp.get(channelDCPKeys[i])))

            elif message == "!speshul":
                send_message("Don't worry," + username)

            elif message == "!cheerup":
                channelCommands.cheerTimer[username] = str(timer.time.time())
                send_message("Oh, you had a bad day " + username + str(channelCommands.dcp.get(channelDCPKeys[i])))

            elif message == "yespls":
                try:
                    yesplsTimeFrame = 20
                    if channelCommands.cheerTimer.get(username) is not None:
                        if (timer.time.time() - float(channelCommands.cheerTimer.get(username))) <= yesplsTimeFrame:
                            send_message(username + str(channelCommands.dcp.get(channelDCPKeys[i])))
                            timer.timeOut[username + message.lower()] = str(timer.time.time())
                except KeyError or AttributeError:
                    send_message(username + str(channelCommands.dcp.get(channelDCPKeys[i])))
                    timer.timeOut[username + message.lower()] = str(timer.time.time())
                return
            else:
                send_message(str(channelCommands.dcp.get(channelDCPKeys[i])))
            timer.timeOut[username + message.lower()] = str(timer.time.time())

        elif sender == "highlight":
            timer.timeOut[username + "!highlight"] = str(timer.time.time())
            try:
                pathRequest = open(channelCommands.pathRequest, "a")
                pathRequest.write("\nHighlight (Day: " + str(timer.datetime.datetime.now()) + ") @" + str(
                    timer.convertToTime(timer.time.time() - bootingTime)) + " " + messageNoRequest)
                pathRequest.close()
                send_message(channelCommands.additionalCommands.get("!highlight"))
            except AttributeError:
                pass
    except FileNotFoundError:
        print("ERROR: File path was not set correctly!")


def calc():
    """
Simple calculator. Older version was more complex, but this is more tedious to code in Python.
    """
    if "*" in message:
        messageSplitUp = message.split("*")
        try:
            send_message(str(float(messageSplitUp[0]) * float(messageSplitUp[1])))
        except ValueError:
            pass
    if "/" in message:
        messageSplitUp = message.split("/")
        try:
            send_message(str(float(messageSplitUp[0]) / float(messageSplitUp[1])))
        except ValueError:
            pass
    if "+" in message:
        messageSplitUp = message.split("+")
        try:
            send_message(str(float(messageSplitUp[0]) + float(messageSplitUp[1])))
        except ValueError:
            pass
    if "-" in message:
        messageSplitUp = message.split("-")
        try:
            send_message(str(float(messageSplitUp[0]) - float(messageSplitUp[1])))
        except ValueError:
            pass


def dice():
    """
Rolls a dice, according to the d they want.
    """
    diceThrown = False
    if message.lower() == "!d2":
        diceThrown = True
        send_message(username + " just rolled a " + str(random.randint(1, 2)) + "!")
    elif message.lower() == "!d3":
        diceThrown = True
        send_message(username + " just rolled a " + str(random.randint(1, 3)) + "!")
    elif message.lower() == "!d4":
        diceThrown = True
        send_message(username + " just rolled a " + str(random.randint(1, 4)) + "!")
    elif message.lower() == "!d6":
        diceThrown = True
        send_message(username + " just rolled a " + str(random.randint(1, 6)) + "!")
    elif message.lower() == "!d8":
        diceThrown = True
        send_message(username + " just rolled a " + str(random.randint(1, 8)) + "!")
    elif message.lower() == "!d10":
        diceThrown = True
        send_message(username + " just rolled a " + str(random.randint(1, 10)) + "!")
    elif message.lower() == "!d12":
        diceThrown = True
        send_message(username + " just rolled a " + str(random.randint(1, 12)) + "!")
    elif message.lower() == "!d20":
        diceThrown = True
        send_message(username + " just rolled a " + str(random.randint(1, 20)) + "!")
    elif message.lower() == "!d100":
        diceThrown = True
        send_message(username + " just rolled a " + str(random.randint(1, 100)) + "!")
    if diceThrown:
        timer.timeOut[username + diceThrow] = str(timer.time.time())


def random_line(file):
    openedFile = open(file)
    allLines = openedFile.read().splitlines()
    sentLine = random.choice(allLines)
    openedFile.close()
    return sentLine


def fileLength(file):
    if os.stat(file).st_size != 0:
        openedFile = open(file)
        with openedFile as fileLine:
            for j, l in enumerate(fileLine):
                pass
        openedFile.close()
        return j + 1
    else:
        return 0


def send_message(sentMessage):
    s.send(bytes("PRIVMSG #" + channel + " :" + sentMessage + "\r\n", "UTF-8"))
    print(sentMessage)


bootingTime = timer.time.time()
receivedMessages = 0

while True:
    line = str(s.recv(1024))
    if "End of /NAMES list" in line:
        break


def curSong():
    """
Calls out only the currently playing song.
    """
    snipFile = open(channelCommands.pathSnip, "r")
    song = snipFile.readline()
    snipFile.close()

    if song != "":
        send_message("Now playing: " + song)


def callOutSong():
    """
Calls out previous and currently playing Song.
    """
    global oldSong

    snipFile = open(channelCommands.pathSnip, "r")
    song = snipFile.readline()
    snipFile.close()

    if song != oldSong:
        if oldSong != "":
            send_message("Previous song was: " + oldSong)
        curSong()
        oldSong = song


# This fine piece of code runs every 3 seconds to check which songs are currently playing.
scheduler = BackgroundScheduler()
scheduler.add_job(func=callOutSong, trigger="interval", seconds=3)
scheduler.start()

while True:
    isBlacklisted = False
    for line in str(s.recv(1024)).split('\\r\\n'):
        parts = line.split(':')
        if len(parts) < 3:
            continue
        if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
            message = parts[2][:len(parts[2])]
        else:
            message = ''

        # Scheduled Announcer:
        if message != '':
            receivedMessages += 1
            if receivedMessages >= quoteMessageRequirement and (timer.time.time() - float(timer.timeOut.get("receivedQuoteTimer"))) >= quoteTimeout:
                timer.timeOut["receivedQuoteTimer"] = str(timer.time.time())

                quoteLength = fileLength(channelCommands.pathQuotes)
                factLength = fileLength(channelCommands.pathFact)
                randInt = random.randint(1, (quoteLength + factLength))
                if randInt >= factLength:
                    send_message(random_line(channelCommands.pathCommands.get("!fact")))
                else:
                    send_message(random_line(channelCommands.pathCommands.get("!quote")))

        username_split = parts[1].split("!")
        username = username_split[0]

        curLine = 1
        blackLength = fileLength(channelCommands.pathBlacklist)
        blackFile = open(channelCommands.pathBlacklist, "r")
        while curLine <= blackLength:
            username.lower()
            curlinestr = blackFile.readline().lower().strip()
            if curlinestr == username.lower():
                blackFile.close()
                isBlacklisted = True
                break
            curLine += 1

        if not isBlacklisted:
            blackFile.close()
            print(username + ": " + message)
            channelCommandsLength = channelCommands.channels.__len__() - 1
            channelComKeys = list(channelCommands.channels.keys())
            channelHahaLength = channelCommands.hahaLinks.__len__() - 1
            channelHahaKeys = list(channelCommands.hahaLinks.keys())
            channelPathLength = channelCommands.pathCommands.__len__() - 1
            channelPathKeys = list(channelCommands.pathCommands.keys())
            channelDCPLength = channelCommands.dcp.__len__() - 1
            channelDCPKeys = list(channelCommands.dcp.keys())
            channelGiveawayLength = channelCommands.giveaway.__len__() - 1
            channelGiveawayKeys = list(channelCommands.giveaway.keys())
            channelSongLength = channelCommands.songCommands.__len__() - 1
            channelSongKeys = list(channelCommands.songCommands.keys())

            # The following loops all go through the dictionaries and post to the channel, while adding a timeout for the
            # user, specified for the command (i.e. a: !youtube -> a can't request Youtube for [cooldown]-seconds).
            i = 0
            while i <= channelCommandsLength:
                if message.lower() == channelComKeys[i]:
                    try:
                        if timer.time.time() - float(timer.timeOut[username + message.lower()]) >= cooldown:
                            schedule_routine("channelCommands")
                    except KeyError:
                        schedule_routine("channelCommands")
                    break
                else:
                    i += 1
            if message.lower() == "!uptime":
                try:
                    if timer.time.time() - float(timer.timeOut[username + message.lower()]) >= cooldown:
                        schedule_routine("uptime")
                except KeyError:
                    schedule_routine("uptime")

            i = 0
            while i <= channelHahaLength:
                if message.lower() == channelHahaKeys[i]:
                    try:
                        if timer.time.time() - float(timer.timeOut[username + message.lower()]) >= cooldown:
                            schedule_routine("hahakeys")
                    except KeyError:
                        schedule_routine("hahakeys")
                    break
                else:
                    i += 1

            # Routine for commands with additional info at the end of the message.
            if message.startswith("!songrequest") or message.startswith("!commandrequest") or message.startswith("!gamerequest"):
                messageSplit = message.split("request")
                messageNoSpace = messageSplit[0].lower()
                messageNoRequest = messageSplit[1]

            elif message.startswith("!shoutout") or message.startswith("!so") and not message.startswith("!song"):
                messageSplit = message.split(" ")
                messageNoSpace = messageSplit[0].lower()
                messageNoRequest = messageSplit[1].lower()

            elif message.startswith("!addquote"):
                messageSplit = message.split("!addquote")
                messageNoSpace = messageSplit[0]
                messageNoRequest = messageSplit[1].strip()
                pathQuote = open(channelCommands.pathQuotes, "a")
                pathQuote.write("\n" + messageNoRequest)
                pathQuote.close()
                send_message(username + " just added '" + messageNoRequest + "' to the roster.")

            elif message.startswith("!highlight"):
                messageSplit = message.split("!highlight")
                messageNoSpace = messageSplit[0]
                messageNoRequest = messageSplit[1].strip()
                try:
                    if (timer.time.time() - float(timer.timeOut[username + "!highlight"])) >= highlightCooldown:
                        schedule_routine("highlight")
                except KeyError:
                    schedule_routine("highlight")
            else:
                messageNoSpace = message.lower()
                messageNoRequest = message

            if message.lower() == "!quote" or message.lower() == "!fact":
                cooldown = quoteCooldown

            i = 0
            while i <= channelSongLength:
                if message.lower() == channelSongKeys[i]:
                    try:
                        if timer.time.time() - float(timer.timeOut[username + message.lower()]) >= cooldown:
                            schedule_routine("song")
                    except KeyError:
                        schedule_routine("song")
                    break
                else:
                    i += 1

            i = 0
            while i <= channelPathLength:
                if messageNoSpace == channelPathKeys[i]:
                    try:
                        if timer.time.time() - float(timer.timeOut[username + message.lower()]) >= cooldown:
                            schedule_routine("request")
                    except KeyError:
                        schedule_routine("request")
                    break
                else:
                    i += 1
            cooldown = cooldownSave

            i = 0
            while i <= channelDCPLength:
                if message.lower() == channelDCPKeys[i]:
                    try:
                        if timer.time.time() - float(timer.timeOut[username + message.lower()]) >= cooldown:
                            schedule_routine("dcp")
                    except KeyError:
                        schedule_routine("dcp")
                    break
                else:
                    i += 1

            i = 0
            while i <= channelGiveawayLength:
                if message.lower() == channelGiveawayKeys[i]:
                    try:
                        if timer.time.time() - float(timer.timeOut[username + message.lower()]) >= cooldown:
                            schedule_routine("giveaway")
                    except KeyError:
                        schedule_routine("giveaway")
                    break
                else:
                    i += 1

            try:
                if timer.time.time() - float(timer.timeOut[username + diceThrow]) >= diceCooldown:
                    dice()
            except KeyError:
                dice()
            break

            calc()
        else:
            print(username + " is blacklisted!")
