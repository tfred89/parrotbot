import os
import sys
import json
import groupy
from groupy.client import Client
from groupy import attachments
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

token = 'kv7Vk1HwnchB319idfHypGutxIwFN0xOByqzsZQb'
client = Client.from_token(token)
bot_id = "477f47d075bc1174ff2aba91e6"

app = Flask(__name__)
@app.route('/', methods=['POST'])
def post():
        data = request.get_json()
        gID = data['group_id']
        bot = bot_id
        group = client.groups.get(gID)
        msg = data['text']
        if '@coffee' in msg:
                at_all(bot, group)
        for y in peeps.keys():
                if y in msg:
                        key = y
                        skwak(bot, key)
        if '@parrot' in msg and 'tags' in message:
                tags(bot)
                
        return "ok", 200

def at_all(bot, group):
        members = group.members
        user_ids = []
        loci = []
        text = ""
        pnt = 0

        for m in members:
                id = m.data['user_id']
                name = "@" + m.data["nickname"] + " "

                user_ids.append(id)

                n = [pnt, len(name)]
                loci.append(n) 
                pnt += len(name)

                text += name

        mention = {}
        mention["user_ids"] = user_ids
        mention["loci"] = loci
        tag = attachments.Mentions(mention['loci'], mention['user_ids'])

        client.bots.post(bot, text, attachments = [tag])

def skwak(bot, key):
        user_ids = peeps[key]
        loci = []
        text = ""
        pnt = 0
        for m in user_ids:
                name = "@" + m.data["nickname"] + " "
                n = [pnt, len(name)]
                loci.append(n) 
                pnt += len(name)
                text += name

        mention = {}
        mention["user_ids"] = user_ids
        mention["loci"] = loci
        tag = attachments.Mentions(mention['loci'], mention['user_ids'])
        client.bots.post(bot, text, attachments = [tag])

def tags(bot):
        text = ""
        for m in peeps.keys():
                text += m + ' '
        client.bots.post(bot, text)

peeps = {'@skwad':['482066', '2513725', '36741', '2513723', '36739'],
         '@frolf':['482066', '8206212', '2513726', '36739', '36740', '30472260', '30685722'],
         '@games':['482066', '8206212', '2513726', '6698773', '30472260', '8206213', '34951757']}


