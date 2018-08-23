import os
import sys
import json
import groupy
from groupy.client import Client
from groupy import attachments
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

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
        if data['name'] != 'Parrot Bot 2.0':
                if '@coffee' in msg:
                        at_all(bot, group)
                for y in peeps.keys():
                        if y in msg.lower():
                                key = y
                                skwak(bot, group, key)
                if '@parrot' in msg and 'groups' in msg:
                        tags(bot)
                if '@parrot' in msg and 'where' in msg:
                        for y in maps.keys():
                                if y in msg.lower():
                                        place = y
                                        places(bot, place)
##                if '@parrot' in msg and 'add' in msg.lower():
##                        user_add(msg)
##
##                if '@parrot' in msg and 'remove' in msg.lower():
##                        user_delete(msg)                                  

                if '@parrot' in msg and 'maps' in msg:
                        spot = ''
                        for i in maps.keys():
                                spot += i + ', '
                        text = 'Where to? If you say "@parrot", "where", and the name of the place, a map will be posted. Current places are: ' + spot
                        client.bots.post(bot, text)
                        
                if 'nsfw' in msg.lower():
                        nsfw(bot)
                                        
                
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
                

def places(bot, place):
        text = 'Check out this map: '
        loc = attachments.Location(name = place + ' ' + maps[place][0], lat=maps[place][1], lng=maps[place][2])
        client.bots.post(bot, text, attachments = [loc])
                

peeps = {'@skwad':['482066', '2513725', '36741', '2513723', '36739', '51268339'],
         '@frolf':['482066', '8206212', '2513726', '36739', '36740', '30472260', '30685722'],
         '@games':['482066', '8206212', '2513726', '6698773', '30472260', '8206213', '34951757', '51268339'],
         '@sk8':['2513725', '482066', '2513726', '2513724', '36739', '2513723', '30685722', '35902999'],
         '@nac':['2513725', '2513718', '2513726', '36741', '2513723', '30472260', '34951757'],
         '@austin':['2513725', '8206189', '482066', '8206212', '2513726', '2513724', '36739', '2513723', '36740', '30472260', '30685722', '35902999']}

 #[address, lat, long]
maps = {'Jeri World':['4706 Clawson Rd, Austin, TX 78745, USA', 30.2216537, -97.78669009999999]}

def user_add(msg):  ## needs work, can't dynaicaly change source file
    try:
            if msg.data['attachments'][0]['type'] == 'mentions':
                    usr_ids = msg.data['attachments'][0]['user_ids']
            for key in peeps:
                    if key in msg:
                        g = key
                        peeps[g].append(user_ids)
    except:
            pass

def user_delete(msg):
    try:
            if msg.data['attachments'][0]['type'] == 'mentions':
                    usr_ids = msg.data['attachments'][0]['user_ids']
            for key in peeps:
                    if key in msg:
                        g = key
                        peeps[g].remove(user_ids)
    except:
            pass						
						

