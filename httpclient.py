import requests


class HTTPClient:
    base_url = 'https://discord.com/api'

    def __init__(self, token):
        self.token = token

    # requests.get() wrapper that inserts the authorization header for Discord
    def get(self, *args, **kwargs):
        headers = kwargs.pop('headers', dict())
        headers['Authorization'] = 'Bot ' + self.token
        kwargs['headers'] = headers
        return requests.get(*args, **kwargs)

    # requests.post() wrapper that inserts the authorization header for Discord
    def post(self, *args, **kwargs):
        headers = kwargs.pop('headers', dict())
        headers['Authorization'] = 'Bot ' + self.token
        kwargs['headers'] = headers
        return requests.post(*args, **kwargs)
