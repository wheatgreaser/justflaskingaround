import flask
from flask import Flask


app = Flask(__name__)

@app.route("/")
def yo():
  return 'yo'

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  


