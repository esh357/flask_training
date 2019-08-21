from flask import Flask, request
app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=['GET', 'POST', 'PUT'])
def hello():
    if request.method == 'POST':
        data = request.form.get('data', 'EMPTY DATA')
        return f'Hello for post request with data: {data}'
    if request.method == 'GET':
        return "Hello for get request"
    return f"Hello for {request.method}!"

if __name__ == "__main__":
    app.run()