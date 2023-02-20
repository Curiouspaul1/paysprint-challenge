from flask import (
    Flask,
    request,
    render_template
)
from flask_mail import (
    Mail,
    Message
)
import requests
import os


app = Flask(__name__)
app.config['MAIL_DEFAULT_SENDER'] = 'paulasalu7@gmail.com'
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'paulasalu7@gmail.com',
    MAIL_PASSWORD = 'otvlbxzmoffanhsn'
))
print(os.getenv('MAIL_PASS'))
_headers = {
    'X-Api-Key': os.getenv('API_KEY')
}
mail = Mail(app)

@app.get('/')
def fetch_news():
    # fetch news
    args = request.args
    if len(args) < 1:
        msg = 'You need to add at least one query param to filter news search'
        return render_template("error.html", data=msg)
    news = requests.get(
        url=os.getenv('URL')+'v2/everything',
        params=args,
        headers=_headers
    )
    if news.status_code != 200:
        return render_template("error.html", data="An unknown error occurred - 400")
    news = news.json()
    return render_template("index.html", news=news['articles'], total=news['totalResults'])


@app.get('/send_news')
def send_news():
    args = request.args
    if len(args) < 1:
        msg = 'You need to add at least one query param to filter news search'
        return render_template("error.html", data=msg)
    news = requests.get(
        url=os.getenv('URL')+'v2/everything',
        params=args,
        headers=_headers
    )
    if news.status_code != 200:
        return render_template("error.html", data="An unknown error occurred - 400")
    msg = Message(
        subject="Paul Asalu - NEWS API CALL",
        recipients=['tech@paysprint.ca'],
        html=render_template("mail.html", news=news.json())
    )
    mail.send(msg)
    return "Message Sent!", 200