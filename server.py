from bottle import route, run
from pymongo import MongoClient
import json

# intializes the mongoDB connection

client = MongoClient()
db = client.documents

# Adds a docs part
docs = db.docs

# Creates data for a new doc
doc_data = {
	'title': 'Random Placeholder Title',
	'content': 'lorum ipsum something something something',
	'owneruid': '1234abcd'
}
# Inserts doc
results = docs.insert_one(doc_data)

# gets requests to the server
@route('/db/<uid>')
def getDoc(uid):
	# logos UID request
	print(uid)
	# returns applicable data to client
	return "Title: " + docs.find_one({'owneruid': uid}).get('title') + " Content: " + docs.find_one({'owneruid': uid}).get('content')

# runs server
run(host='localhost', port=8080, debug=True)