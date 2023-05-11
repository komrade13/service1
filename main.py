from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/time')
def current_time():
    return datetime.now().strftime("The current date and time is %Y-%m-%d %H:%M:%S")

@app.route('/info')
def info():
    info_str = "This is a sample Python web app running on Google App Engine. It has two routes: '/' and '/time'. The '/' route returns 'Hello, World!', while the '/time' route returns the current date and time."
    return info_str

if __name__ == '__main__':
    app.run()
