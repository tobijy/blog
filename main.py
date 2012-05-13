from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/blog/')
def blog():
	return render_template('blog.html')

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
