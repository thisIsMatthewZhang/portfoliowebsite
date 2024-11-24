from flask import Flask, render_template, redirect, url_for, request
import csv

app = Flask(__name__)
print(__name__)

@app.route('/') # URL parameters
def my_home():
	return render_template('index.html') # render_template() automatically searches for a folder called 'templates' containing html doc

# export FLASK_APP=<server filename>
# flask run
# DEBUG MODE: flask --app <server name> run --debug

@app.route('/<string:page_name>')
def html_page(page_name=None):
	return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	try:
    		data = request.form.to_dict()
    		write_to_csv(data)
    		return redirect('/thankyou.html#contact')
    	except:
        	return 'did not save to database'
    else:
    	return 'something went wrong'

def write_to_file(data):
	with open('portfoliodatabase.txt','a') as database:
		name = data['name']
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{name},{email},{subject},{message}')

def write_to_csv(data):
	with open('portfoliodatabase.csv','a', newline='') as database2:
		name = data['name']
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,email,subject,message])
