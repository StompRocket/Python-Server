from bottle import route, run
from pymongo import MongoClient
import json

client = MongoClient()
db = client.documents

docs = db.docs

doc_data = {
	'title': 'Random Placeholder Title',
	'content': 'lorum ipsum something something something',
	'owneruid': '1234abcd'
}
results = docs.insert_one(doc_data)

@route('/db/<uid>')
def getDoc(uid):
	print(uid)
	return "Title: " + docs.find_one({'owneruid': uid}).get('title') + " Content: " + docs.find_one({'owneruid': uid}).get('content')

run(host='localhost', port=8080, debug=True)