from flask import Flask,g,request,render_template,redirect,url_for,flash
from pymongo import Connection
from bson.objectid import ObjectId
#import time

app=Flask(__name__)
app.debug = True
app.secret_key = '\x86\xdb;\x91\x9dQfX4\x151\xc0\xf1\x9c\xc1\xac\x87\xb1uk\x19$\xd0\xbb'

@app.before_request
def before_request():
	conn = Connection()
	g.db = conn.test

def get_lists():
	return g.db.lists.find()

#def finish_list(list_id):
#	return g.db.lists.remove({'_id':ObjectId(list_id)})

@app.route('/',methods=['GET','POST'])
def to_do_list():
	show = get_lists()
	if request.method == 'POST':

		if not request.form['title']:
			flash('Title can not be empty','warning')
			return redirect(url_for('to_do_list'))
#			return 'Title can not be empty'

		if request.form['title']:
			title=request.form['title']
			g.db.lists.insert({'title':title})
			flash('Add list successfully','success')
			return redirect(url_for('to_do_list'))
		else:
			flash('Failed to add list','danger')
			return redirect(url_for('to_do_list'))
	return render_template('index.html',lists=show)
'''
		if request.form['title']:
			title=request.form['title']
			g.db.lists.insert({'title':title})
			return redirect(url_for('to_do_list'))
		else:
			return'Title can not be empty'
	return render_template('index.html',lists=show)
'''
@app.route('/finish_list/<list_id>')
def finish_list(list_id):
	g.db.lists.remove({'_id':ObjectId(list_id)})
	return redirect(url_for('to_do_list'))

if __name__ == '__main__':
	app.run()