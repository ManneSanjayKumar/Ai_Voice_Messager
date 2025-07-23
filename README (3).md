
# 🗣️ AI Voice Messenger - Flask Web App

This is a Flask-based AI Voice Messenger application that allows users to:
- Register and login
- Type a message
- Convert it into speech using **gTTS**
- Schedule the audio to be sent to the **admin's email** at 8:00 AM daily

---

## 🚀 Features

- 🔐 User Registration & Login System
- 🧠 Text-to-Speech using **gTTS**
- ⏰ Message scheduling with **APScheduler**
- 📧 Sends all messages to the admin via email
- 📂 Stores voice files locally (`/static/voice/`)
- 👤 Admin-only email access to scheduled messages

---

## 📸 Screenshots

> (Add screenshots of your dashboard, message preview, and email)

---

## ⚙️ Technologies Used

- Python 3.x
- Flask
- Flask-APScheduler
- gTTS (Google Text-to-Speech)
- smtplib & EmailMessage (for sending email)
- HTML / CSS (for frontend)

---

## 📁 Project Structure

```
project/
│
├── static/
│   └── voice/               # Stores generated .mp3 files
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   └── preview.html
│
├── app.py                   # Main Flask application
├── README.md                # Project documentation
```

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-voice-messenger.git
cd ai-voice-messenger
```

### 2. Install required packages
```bash
pip install Flask Flask-APScheduler gTTS
```

### 3. Configure Email Settings

In `app.py`, update the following:

```python
ADMIN_EMAIL = '21eg110b21@anurag.edu.in'       # Your admin email
SENDER_EMAIL = 'your_gmail@gmail.com'          # A Gmail account you control
SENDER_PASSWORD = 'your_16_digit_app_password' # Gmail app password
```

> 📌 You **must enable 2-Step Verification** on your Gmail and use an [App Password](https://support.google.com/accounts/answer/185833) for security.

---

### 4. Run the app
```bash
python app.py
```

The app will run at:  
`http://127.0.0.1:5000`

---

## 🕒 Scheduler Info

- The app uses `APScheduler` to send all collected messages every day at **8:00 AM**.
- Voice messages are emailed to the **admin's inbox** as `.mp3` attachments.

---

## 🔐 Future Improvements

- Admin dashboard to view all messages
- User message history page
- Email status tracking
- Voice call integration (e.g., Twilio / Plivo / Exotel)

---

## 📩 Contact

- Admin Email: [21eg110b21@anurag.edu.in](mailto:21eg110b21@anurag.edu.in)

---

## 📜 License

This project is for educational use only.  
You are free to modify and use it for personal or academic projects.
