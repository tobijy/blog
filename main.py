from datetime import datetime

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	content = db.Column(db.Text)
	pub_date = db.Column(db.DateTime)
	year = db.Column(db.Integer)
	month = db.Column(db.Integer)
	day = db.Column(db.Integer)

	def __init__(self, title, content):
		self.title = title
		self.content = content
		pub_date = datetime.utcnow()
		self.pub_date = pub_date
		self.year = pub_date.year
		self.month = pub_date.month
		self.day = pub_date.day

	def __repr__(self):
		return '< Post %r>' % self.title

	

@app.route('/')
@app.route('/blog/')
def blog():
	return render_template('blog.html', posts=Post.query.all())

@app.route('/post/<int:year>/<int:month>/<path:title>/')
def post(year,month, title):
	return "post xyz"

@app.route('/archive/')
def archive():
	return "Archive"

@app.route('/contact/')
def contact():
	return render_template('contact.html')

@app.errorhandler(404)
def page_not_found_404(error):
	return error;

@app.route('/admin/')
def admin():
	return render_template('admin.html')

if __name__ == "__main__":
	# turn debug mode on
	app.debug = True

	app.run()
