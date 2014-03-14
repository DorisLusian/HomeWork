from pymongo import Connection

conn = Connection()
db = conn.test 
db.drop_collection('lists')

admin = {'title': 'aaaaaaaa',  'create_at': '2014-3-10'}
db.lists.insert(admin)

