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