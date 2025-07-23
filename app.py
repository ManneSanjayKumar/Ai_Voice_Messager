from flask import Flask, render_template, request, redirect, url_for, session, flash
from gtts import gTTS
from flask_apscheduler import APScheduler
import os
import smtplib
from email.message import EmailMessage
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret_key'

# APScheduler config
class Config:
    SCHEDULER_API_ENABLED = True

app.config.from_object(Config())
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

# Dummy user store
users = {}

# Store scheduled messages
scheduled_messages = []

# Admin email config
ADMIN_EMAIL = '21eg110b21@anurag.edu.in'
SENDER_EMAIL = '21eg110b21@anurag.edu.in'
SENDER_PASSWORD = 'quie wtir clcy tjdm'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users[email] = password
        flash('Registered successfully. Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if users.get(email) == password:
            session['email'] = email
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials.', 'danger')
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/generate', methods=['POST'])
def generate():
    if 'email' not in session:
        return redirect(url_for('login'))

    message = request.form['message']
    filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{session['email'].replace('@', '_')}.mp3"
    filepath = os.path.join('static', 'voice', filename)

    tts = gTTS(text=message, lang='en')
    tts.save(filepath)

    return render_template('preview.html', filename=filename, message=message)

@app.route('/send', methods=['POST'])
def send():
    if 'email' not in session:
        return redirect(url_for('login'))

    filename = request.form['filename']
    message = request.form['message']
    filepath = os.path.join('static', 'voice', filename)

    scheduled_messages.append({
        'user': session['email'],
        'message': message,
        'filepath': filepath
    })

    flash('✅ Message sent to Admin and scheduled for 8:00 AM.', 'success')
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# Background job to send messages
@scheduler.task('cron', hour=8, minute=0)
def send_scheduled_emails():
    global scheduled_messages
    if not scheduled_messages:
        return

    msg = EmailMessage()
    msg['Subject'] = 'Scheduled Voice Messages'
    msg['From'] = SENDER_EMAIL
    msg['To'] = ADMIN_EMAIL
    msg.set_content('Attached are the scheduled voice messages from users.')

    for item in scheduled_messages:
        with open(item['filepath'], 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(item['filepath'])
            msg.add_attachment(file_data, maintype='audio', subtype='mpeg', filename=file_name)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        print("Scheduled messages sent.")
    except Exception as e:
        print("Failed to send:", e)

    scheduled_messages = []

if __name__ == '__main__':
    if not os.path.exists('static/voice'):
        os.makedirs('static/voice')
    app.run(debug=True)    
