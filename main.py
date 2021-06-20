# Sample file
from client import Client


# Initialize the Discord client
disc = Client('discord_credentials.json')

# Send a message to a channel ID
channel = 12345
channel_msg = 'Hello Channel World'
disc.send(channel, channel_msg)

# Send a DM to a user ID
user = 98765
user_msg = 'Hello User World'
disc.dm(user, user_msg)
