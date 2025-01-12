# -*- coding: utf-8 -*-

import json

import requests


class Github(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        response = requests.get(
            'https://api.github.com/',
            auth=(self.username, self.password))

    @property
    def user(self):
        response = requests.get('https://api.github.com/users/%s' % self.username)
        content = response.content
        data = json.loads(content)
        user = User(data, self)
        return user

class User(object):
    _keys = ['name', 'email']

    def __init__(self, data, gh):
        self.gh = gh
        for key in self._keys:
            setattr(self, key, data[key])
    @property
    def repos(self):
        response = requests.get(
            'https://api.github.com/user/repos',
            auth=(self.gh.username, self.gh.password))
        content = response.content
        data = json.loads(content)
        return data
