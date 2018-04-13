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

