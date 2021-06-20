from httpclient import HTTPClient
import json


class Client(HTTPClient):
    def __init__(self, token_file):
        with open(token_file, 'r') as f:
            token = json.load(f)['discord_key']
        super().__init__(token)
        self.dm_ids = dict()

    # Send a message to a channel
    def send(self, channel_id, message):
        url = self.base_url + f'/channels/{channel_id}/messages'
        data = {
            'content': message
        }
        self.post(url, json=data)

    # DM a user a message
    def dm(self, user_id, message):
        channel_id = self.dm_ids.get(user_id) or self._create_user_channel(user_id)
        self.send(channel_id, message)

    # Supporting functions
    # Create a user channel (DM)
    def _create_user_channel(self, user_id):
        url = self.base_url + '/users/@me/channels'
        data = {
            'recipient_id': user_id
        }
        dm_data = self.post(url, json=data)
        print(dm_data.text)
        dm_id = dm_data.json()['id']
        self.dm_ids[user_id] = dm_id
        return dm_id
