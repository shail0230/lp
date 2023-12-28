from flask import Flask, request, url_for, redirect, render_template,jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__, template_folder='templates')

client = MongoClient('mongodb+srv://harry:evan12345@cluster0.nfvrm5c.mongodb.net/?retryWrites=true&w=majority')

db = client['landing_page']
collection = db['appointment']

#app.config["MONGO_URI"] = ""
#mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_appointment', methods=['POST'])
def submit_appointment():
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        # Insert data into MongoDB
        appointment_data = {
            'date': date,
            'time': time,
            'name': name,
            'phone': phone,
            'email': email
        }
        collection.insert_one(appointment_data)

        # Redirect to a success page or back to the form
        return redirect(url_for('success'))

@app.route('/success')
def success():
    return 'Thank You For Appointment , Our Team Will Contact You Soon !!'

if __name__ == '__main__':
    app.run(debug=False)
