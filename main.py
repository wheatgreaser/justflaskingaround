import flask
from flask import Flask, render_template, url_for, request
import time
from datetime import datetime

app = Flask(__name__)

time = datetime.now()
count = 12
coolList = []

@app.route("/", methods=['GET', 'POST'])
def coolthing():
  time = datetime.now()
  if request.method == 'POST':
    name = request.form.get('name')
    coolList.append(name)
    time = datetime.now()
  return render_template('index.html', coolList = coolList, count = count, senttime = time)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  


