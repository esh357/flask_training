from flask import render_template, request
from webapp import app


@app.route('/')
def index():
    return "Hello to the World of Flask!"


@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/hello/<name>')
def hello_name(name=None):
    return "Hello {name}".format(name=name)


@app.route('/hello/<int:number>')
def hello_number(number=0):
    return "Hello number: {number}".format(number=number)

@app.route('/hello/<float:number>')
def hello_float_number(number=0.0):
    return "Hello float number: {number}".format(number=number)


@app.route('/html')
@app.route('/html/<user>')
def html(user=None):
    user = user or 'Rahul'
    return '''
        <html>
            <head>
                <title>Flask Framework Training</title>
            </head>
            <body>
                <h4>Hello %s!</h4>
                <p>Welcome to the world of Flask!</p>
            </body>
        </html>
    ''' % user


@app.route('/<user>', methods=['GET', 'POST'])
def user_index(user=None):
    user = user or "srahul07"
    external_image = "https://picsum.photos/id/237/200/300"
    said = 'said nothing yet!'
    if request.method == 'POST':
        said = request.form.get('said_it')
    return render_template("index.html", user=user,
                           external_image=external_image, said=said)
