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
	'owneruid': '2'
}

doc_data2 = {
	'title': 'Another Title',
	'content': 'Sweededn Is Good',
	'owneruid': '1'
}

docs.insert_many([doc_data1, doc_data2])

# gets requests to the server
@route('/db/<uid>')
def getDoc(uid):
	# logos UID request
	print(uid)
	# returns applicable data to client
	return "Title: " + docs.find_one({'owneruid': uid}).get('title') + " Content: " + docs.find_one({'owneruid': uid}).get('content')

@route('/push/t/<title>/c/<content>/u/<uid>')
def pushDoc(title, content, uid):
	docs
	# logos UID request
	print(uid)
	pushDoc = {
		'title': title,
		'content': content,
		'owneruid': uid
	}

	docs.insert_one(pushDoc)
	return "pushed data successfully to DB"

# runs server
run(host='localhost', port=8080, debug=True)