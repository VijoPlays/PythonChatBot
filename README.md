# Python Chat bot ![build](https://github.com/VijoPlays/PythonChatBot/actions/workflows/codeql-analysis.yml/badge.svg) [![Python safety check](https://github.com/VijoPlays/PythonChatBot/actions/workflows/safety.yml/badge.svg)](https://github.com/VijoPlays/PythonChatBot/actions/workflows/safety.yml)

## About

This is a Python chat bot that you can use to monitor and respond to messages sent by viewers on your Twitch Account.
I tried to make it as easy as possible to add more to the bot (e.g. by simply adding new files in the channelCommands file).

This bot will respond to commands (where the commands can be put on cooldown automatically afterwards, so that the viewers can not abuse them). If you want to use the song functionality, you'll have to run Snip and either iTunes or Spotify in the background (or whatever else program runs with Snip; at the time of making this project these are the only 2 available music players). Some paths have to be adjusted (obviously) in the channelCommands file, but even there I made moving the files as easy as possible. Just change genericPath and pathSnip to your needs.
The name of the channel the bot should be on can be adjusted by changing the channel variable in the main file. You will have to create a second account and get the oauth and insert that one in the auth variable. Then you just run the bot and everything should go smoothly from here.

DISCLAIMER: This bot was not written to be fast/good/efficient. It was mostly a fun project I wanted to spend time with, where I ported my mIRC chatbot over to Python, while exploring what Python offered. It should still work, but my main goal was to find out how certain things worked in Python and to toy around with it a bit.

## Installation

In order to run this, you'll need to install Python3 onto your PC. Windows users can use the official installer from the [Python-website](https://www.python.org/downloads/). Ifm you use Linux, you might already have it, if not - a simple 'How to install Pyhton [distribution]' should do the trick (depending on your package manager).

After that, you will only have to open a terminal and type:

> python3 run main.py

You might have to type 'python' instead of 'python3'.

This command just runs the main python file, as long as the terminal is opened.

### Configuration

Before running the script, you'll have to go into the main.py file and change some parameters, like the channel urls and your tokens.
