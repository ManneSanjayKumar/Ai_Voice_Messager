# 🗣️ AI Voice Messenger - Flask Web App

This project is a web-based AI Voice Messenger system built using **Flask**, **gTTS (Google Text-to-Speech)**, and **Flask-APScheduler**. It allows any registered user to type a message, convert it to speech, and schedule it to be sent as an audio attachment to the admin's email daily at 8:00 AM.

---

## 📌 Key Functionalities

- 👥 User Registration & Login
- 🗨️ Message input and preview
- 🎤 Text-to-Speech conversion (using gTTS)
- 🕒 Scheduling voice messages (Flask APScheduler)
- 📧 Email delivery to admin with audio attachments (.mp3)

---

## 🗂️ Project Structure

```
ai-voice-messenger/
│
├── static/
│   └── voice/                   # 📁 Stores generated voice .mp3 files
│
├── templates/                   # 📁 HTML templates for all pages
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   └── preview.html
│
├── app.py                       # 🧠 Main application logic (Flask backend)
├── README.md                    # 📄 Project documentation
```

---

## 🛠️ Setup Instructions

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/ai-voice-messenger.git
cd ai-voice-messenger
```

### ✅ Step 2: Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### ✅ Step 3: Install Required Libraries

```bash
pip install Flask Flask-APScheduler gTTS
```

> You can also use a `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

## ✉️ Email Configuration

Open `app.py` and configure the email section with:

```python
ADMIN_EMAIL = '21eg110b21@anurag.edu.in'         # 📥 Receiver (admin)
SENDER_EMAIL = 'your_gmail@gmail.com'            # 📤 Sender (your Gmail)
SENDER_PASSWORD = 'your_16_digit_app_password'   # 🔑 Gmail App Password
```

> 🔒 Make sure to use an [App Password](https://support.google.com/accounts/answer/185833) generated from your Gmail account (2-Step Verification must be ON).

---

## 🚀 Running the Application

```bash
python app.py
```

Visit your app at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💡 Usage Workflow

### 🧑‍💻 For Users:
1. **Register** at `/register`
2. **Login** at `/login`
3. On the **Dashboard**, type your message
4. Click **Generate** to convert the message to `.mp3`
5. Preview the voice output
6. Click **Send** to schedule the message

### 📁 File Saving Format:
- Files are saved in `static/voice/` directory
- Format: `YYYYMMDD_HHMMSS_useremail.mp3`
- Example: `20250723_110233_user_gmail_com.mp3`

---

## ⏰ Scheduled Task Details

- A background job is configured using **Flask-APScheduler**
- Executes **every day at 8:00 AM**
- Collects all scheduled messages and sends them as `.mp3` email attachments to the admin

---

## 📧 Example Email Content

- Subject: `Scheduled Voice Messages`
- From: `your_gmail@gmail.com`
- To: `21eg110b21@anurag.edu.in`
- Body: "Attached are the scheduled voice messages from users"
- Attachments: `.mp3` voice files

---

## 🔮 Future Enhancements

- Admin dashboard with history and status
- Voice call integration (Twilio/Plivo)
- Real-time email notifications
- SQLite database integration

---

## 👨‍💼 Author

- **Admin Email**: [sanjaykumarmanne@gmail.com]



## 📝 License

This project is for academic and personal use.  
Free to use, customize, and improve with credits.

