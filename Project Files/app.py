from flask import Flask, render_template, request


app = Flask(__name__)#initializing the flask app


@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True, port=8000)