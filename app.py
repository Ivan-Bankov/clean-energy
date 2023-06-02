from flask import Flask, render_template, request, flash
from email.mime.text import MIMEText
import smtplib
from dotenv import dotenv_values

config = dotenv_values(".env")

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/form", methods=['POST', 'GET'])
def form():
    name = request.form.get("name")
    sender = request.form.get("email")
    details = request.form.get("message")
    receiver = "support@clean.energy"
    message = f"""\
    Subject: Email Test by {name}
    To: {receiver}\n
    From: {sender}\n\n

    {details}"""
    host = config['MAIL_HOST']
    port = config['MAIL_PORT']
    username = config['UNAME']
    password = config['PASS']
    msg = MIMEText(message, 'html')
    with smtplib.SMTP(host, port) as server:
        server.login(username, password)
        server.sendmail(sender, receiver, msg.as_string())
    
    return render_template("index.html")

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)