# ct4nk3r-meme-bot

authentication should happen in a different file:

```
#authentication.py

import praw
def reddit_authentication():
    print("Authenticating...")
    reddit = praw.Reddit(client_id="client_id",
                     client_secret="secret",
                     username="username-meme-bot",
                     password="password",
                     user_agent="bot made by u/username")
    return reddit

def discord_authentication():
    return 'DISCORD_TOKEN'
#token should be at https://discord.com/developers/applications/00000000000000/bot -> token -> copy
```

Added a few functions into cogs instead of using the main line:

```
Dice:
    r           Rolls a dice using ndN format.
Functions:
    countdown   counting down from 10 to 0
    status      Change status of the bot
Test:
    hello       hello command for the bot
    ping        Writes back Pong in response
    roll        Simulates rolling dice.
Main:
    meme        sends the newest meme into chat from r/memes
```