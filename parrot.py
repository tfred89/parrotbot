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
bot_id = "1ebecf67b694992ac5f7821a07"

app = Flask(__name__)
@app.route('/', methods=['POST'])
def post():
        data = request.get_json()
        gID = data['group_id']
        bot = bot_id
        group = client.groups.get(gID)
        msg = data['text']
        if data['name'] != 'Parrot Bot 2.0 - The Squawkening':
                if '@coffee' in msg:
                        at_all(bot, group)
                for y in peeps.keys():
                        if y in msg:
                                key = y
                                skwak(bot, group, key)
                if '@parrot' in msg and 'tags' in msg:
                        tags(bot)
                if '@parrot' in msg and 'where' in msg:
                        for y in maps.keys():
                                if y in msg:
                                        place = y
                                        places(bot, place)
                                        
                
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

def skwak(bot, group, key):
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

def tags(bot):
        text = ""
        for m in peeps.keys():
                text += m + ' '
        client.bots.post(bot, text)

def places(bot, place):
        text = 'Check out this map'
        loc = attachments.location(name = place + maps[place][0], lat=maps[place][1], lng=maps[place][2])
        client.bots.post(bot, text, attachments = loc)
                

peeps = {'@skwad':['482066', '2513725', '36741', '2513723', '36739', '51268339'],
         '@frolf':['482066', '8206212', '2513726', '36739', '36740', '30472260', '30685722'],
         '@games':['482066', '8206212', '2513726', '6698773', '30472260', '8206213', '34951757', '51268339'],
         '@sk8':['2513725', '482066', '2513726', '2513724', '36739', '2513723', '30685722', '35902999']}

maps = {'Jeri World':['4706 Clawson Rd, Austin, TX 78745, USA', 30.2216537, -97.78669009999999]} #[address, lat, long]



