from flask import Flask
app = Flask(__name__)

@app.route("/")  # What's a decorator doing here. Is there an alternative
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()