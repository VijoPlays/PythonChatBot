# Path variables will be put here, because me smart, only gotta change genericPath instead of all of them
genericPath = "G:\\Program Code\\python\\Hellbot\\resources\\"
pathSnip = "H:\\Videos\\Snip\\Snip\\Snip.txt"
pathGrats = genericPath + "grats.txt"
pathSchedule = genericPath + "scheduledannouncer.txt"
pathRequest = genericPath + "request.txt"
pathFact = genericPath + "facts.txt"
pathRoast = genericPath + "roast.txt"
pathQuotes = genericPath + "quote.txt"
pathYesno = genericPath + "yesno.txt"
pathDCP = genericPath + ""
pathRecipes = genericPath + "recipes.txt"
# Feel free to add people into this document to blacklist their user names. They can't interact with the bot after that anymore.
pathBlacklist = genericPath + "blacklist.txt"

# Put generic channels here.
channels = {
    "!youtube": "https://www.youtube.com/c/vijoplays",
    "!shitpost": "https://www.youtube.com/channel/UCO_DdW0vb0k7P2fpwm5MXSw/",
    "!twitter": "https://twitter.com/VijoPlays",
    "!twitch": "https://www.twitch.tv/vijoplays",
    "!anook": "https://www.anook.com/vijo",
    "!steam": "http://steamcommunity.com/id/Vijo",
    "!reddit": "https://www.reddit.com/user/VijoPlays/",
    "!battlenet": "http://eu.battle.net/wow/en/character/Argent%20Dawn/Vija/advanced",
    "!discord": "https://discordapp.com/invite/uHp93ff"
}

# Put commands with Path variables here. Game/Song/Command all use a "request"-suffix, but the code doesn't allow this.
pathCommands = {
    "*grats*": pathGrats,
    "!fact": pathFact,
    "!roast": pathRoast,
    "!quote": pathQuotes,
    "!recipe": pathRecipes,
    "!randdomquote": pathQuotes,
    "!shalli": pathYesno,
    "!schedule": "BEWARE: THIS IS THE OLD SCHEDULE - CURRENTLY THERE IS NO SCHEDULE: ",
    "!game": "Thank you very much for your contribution & interest, comrade. Vijo will take a look and might just play it!",
    "!song": "Thank you very much for your contribution & interest, comrade. It might take some time until this song appears in the playlist, German laws and such... *grr*",
    "!command": "Thank you very much for your interest, comrade! Vijo will take a look and see if he can implement such a weird command...",
    "!shoutout": "",
    "!so": ""
}

# Put unique 'interactions' here.
hahaLinks = {
    "!instagram": "Vijo is sorry, but for now he does not participate in such mainstream tasks!",
    "!merch": "As if I could afford merch, lol.",
    "!snapchat": "[Insert text from !instagram into this one.]",
    "!patreon": "Although Vijo doesn't like this, I'm just going to drop the requested link here... He just created "
                "it because 'why not' - not for profit or anything, just because he already had a Patreon account "
                "anyway: https://www.patreon.com/VijoPlays",
    "!donate": "",
    "!zelda": "What if Zelda...? http://i.imgur.com/fEi2Yoz.jpg",
    "!boobs": "http://i.imgur.com/OsJJRQC.gif",
    "!fluff": "Here you go! I hope this will help you get through the day. <3 (https://youtu.be/kaVENZWnCYs)",
    "*shrug*": "¯\_(ツ)_/¯",
    "!imgur": "Here you go, click the link for a random Imgur link (beware: if your filter is not active you might stumble upon a NSFW post) : https://goo.gl/dVLBCM",
    "!wikipedia": "Here you go, click the link for a random Wikipedia article: https://goo.gl/oKPHsp",
    "!commands": "Here's the list of things I listen to *rawr*: https://docs.google.com/document/d/1yg9t_kCep2T_sQEX9eu0d8q_Kb6I9zwH9ifDjjHZHLs/edit - Alternatively you can always click 'The Bot' to the left. ",
    "!playlist": "Here's the link to my playlist: https://play.spotify.com/user/blfasan/playlist/2af92Mg3Xa59DjIDl1nmfR",
    "!camping": "As long as you say 'no homo', having 3 d*cks in your mouth does not necessarily mean that you're gay... That's at least what my dad always told me when we went on a camping trip!",
    "!cardgame": "Playing a Children's card game is like making love. It's always on a table and you'll feel deep shame afterwards! Also, the older you get, the less fun it is. So remember, always wear a condom when playing card games."
}

# Put giveaway commands here.
giveaway = {
    "!join": "",
    "!players": "",
    "!winner": "",
    "!timeleft": "",
    "!giveaway": "",
    "!cancelgiveaway": ""
}

# Dragon Canadian Pesos. Loyalty 'system' of Vijo.
dcp = {
    "!dcp": "Dragon Canadian Pesos. A valuable resource that only the rich can get by watching this channel.",
    "!useless": "Well, thanks for that. This command is useless as the title says. Now you spend time and effort to do something useless! Well, might as well just keep on watching Vijo play. He's uesless after all, too!",
    "!waste": " just wasted 1 Canadian Peso in order to write this message, I hope he/she/it is proud!",
    "!speshul": " you ARE special! <3 (Thanks for using our services to transfer Canadian Pesos to people that need them.",
    "!assurance": "Who's the man, my friend? YOU ARE! https://cdn.meme.am/cache/instances/folder190/65967190.jpg (This command costs you Canadian Pesos and makes Vijo richer, or something like that atleast.)",
    "!cheerup": " ? For just 20 Canadian Pesos (an incredibly expensive ressource) I can help you feel better! Type yespls if you want that.",
    "yespls": " thanks for your donation of 20 Canadian Pesos! You are indeed a perfect human being and I hope everything will be better from now on for you!"
}

cheerTimer = {
}

giveawayPlayers = {
}

songCommands = {
    "!song": "",
    "!rate": "",
    "!ratings": ""
}

# These are commands that are handled in the main method themselves already.
additionalCommands = {
    "!highlight": "Thank you very much for your contribution, comrade! This makes it easier for me and Vijo to create highlights, however, remember that you can also create clips yourself and send them to Vijo.",
    "!uptime": "",
    "!songrequest": "",
    "!commandrequest": "",
    "!gamerequest": "",
    "!d2 up to !d20": "",
    "simple calculations": ""
}
