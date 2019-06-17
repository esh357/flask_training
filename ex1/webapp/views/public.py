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
                <h1>Hello %s!</h1>
                <p>Welcome to the world of Flask!</p>
            </body>
        </html>
    ''' % user

