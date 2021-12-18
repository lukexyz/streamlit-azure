from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, welcome to flaskcozom. Where all your dreams come true."


if __name__ == '__main__':
    app.run(debug=True)