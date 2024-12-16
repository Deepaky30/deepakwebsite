from flask import Flask, request, render_template
from flask_mail import Mail, Message
from flask import Flask, send_from_directory

app = Flask(__name__)

# Configure email settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'deepakyadavk2951@gmail.com'
app.config['MAIL_PASSWORD'] = 'eror zghl ceez umqe'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Send email
    msg = Message('New Form Submission', sender='deepakyadavk2951@gmail.com', recipients=['deepakyadavk2951@gmail.com'])
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    mail.send(msg)

    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)