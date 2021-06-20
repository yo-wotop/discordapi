# DiscordAPI

A simple, **synchronous** wrapper to make basic calls to the Discord API.  

## Why?

The [core Discord API](https://discord.com/developers/docs/intro) is a poorly-documented mess. I can't imagine how bots and other infrastructure have been made around this documentation unless they were aided by the Discord team or reverse-engineered about half of the calls.

To make matters worse, attempting to search for help with the Discord API just gets you people recommending the various pre-made asynchronous bot libraries (such as [discord.py](https://github.com/Rapptz/discord.py)). These libraries are great -- robust, well-documented, and overall fantastic if you want to make an entire bot.

What if you just want to make a simple notification system? Something triggered and you want your bot to send you a DM? You'll spend hours trying to work through the synchronous/asynchronous garbage on every small update, trying to remember to use `asyncio.run_coroutine_threadsafe()`, etc. My other repositories ([simple-discord-client](https://github.com/yo-wotop/simple-discord-client) / [simple-discord-server](https://github.com/yo-wotop/simple-discord-server)) attempt to remedy this a bit, and are still useful if you want to create a a more robust _bot infrastructure_ with normalized bot commands and a variety of people that are authorized to use it (without sharing your Discord token with them), but overkill for just a simple notification system.

Hence, this repo. Here, you can just call base functionality like **sending messages to channels** and **DMing users** with no additional setup.

## Installation

Installation on this is pretty simple:

```shell
git clone https://github.com/yo-wotop/discordapi.git
cd discordapi
pip install -r requirements.txt
```

Though, realistically the requirements are just that you have `requests`.

## Usage

Usage is trivially easy.

First, modify the included `discord_credentials.json` file to have your Discord authentication token.

Once that's set up, the functionality will just **work**. Want to send a message to channel `12345`?

```python
from discordapi import Client


client = Client('discord_credentials.json')

channel = 12345
msg = 'Hello World'
client.send(channel, msg)
```

Want to DM user `98765`?

```python
from discordapi import Client


client = Client('discord_credentials.json')

user = 98765
msg = 'Hello World'
client.dm(user, msg)
```

Feel free to just modify the sample file (`main.py`). 