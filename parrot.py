import os
import sys
import json
from groupy.client import Client
from groupy import attachments
from flask import Flask, request
from datetime import datetime
from groups import peeps



token = os.environ['gm_key']
client = Client.from_token(token)
bot_id = '1ebecf67b694992ac5f7821a07'

app = Flask(__name__)
@app.route('/', methods=['POST'])
def post():
        data = request.get_json()
        gID = data['group_id']
        bot = bot_id
        group = client.groups.get(gID)
        msg = data['text']
        if data['sender_type'] != 'bot':
                if '@coffee' in msg:
                        at_all(bot, group)
                for y in peeps.keys():
                        if y in msg.lower():
                                key = y
                                skwak(bot, group, key)
                if '@parrot' in msg and 'groups' in msg:
                        tags(bot)

                if 'nsfw' in msg.lower():
                        nsfw(bot)

                if '@jeff' in msg:
                    jeff_gone(bot)

        return "ok", 200

def at_all(bot, group):  ##sends mention to all members of group
        members = group.members
        user_ids = []
        loci = []
        text = ""
        pnt = 0

        for m in members:
                id = m.data['user_id']  ## pulls all user IDs
                name = "@" + m.data["nickname"] + " "  ##creats text variable for each member

                user_ids.append(id)  ## adds user to list

                n = [pnt, len(name)]  ## loci list of member
                loci.append(n) ## adds member and loci to list
                pnt += len(name)  ## goes to next available point in loci

                text += name  ## text variable added to list

        mention = {}  ## creates mention dictionary with userID as the key and loci as the value
        mention["user_ids"] = user_ids
        mention["loci"] = loci
        tag = attachments.Mentions(mention['loci'], mention['user_ids'])  ## creates mention attachments

        client.bots.post(bot, text, attachments = [tag])

def skwak(bot, group, key):  ## creates tags for specific groups with 'key' being the specific group
        members = group.members
        user_ids = []
        loci = []
        text = ""
        pnt = 0
        for m in members:
                id = m.data['user_id']
                if id in peeps[key]:
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

def tags(bot):  ## prints all available groups to be called
        text = ""
        for m in peeps.keys():
                text += m + ' '
        client.bots.post(bot, text)

def nsfw(bot):
        text = '.'
        for m in range(10):
                client.bots.post(bot, text)


def jeff_gone(bot):
    left = int('1523287374')
    now = datetime.now().timestamp()
    td = str(int((now - left)/(60*60*24)))
    text = "Jeff has been gone for %s days. He's not coming back." % td
    client.bots.post(bot, text)
