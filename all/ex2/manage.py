import os

from flask_script import Manager, Server
import webapp
from webapp import app
from webapp.utils import get_configurations


if __name__ == "__main__":
    config = get_configurations("{0}.cfg".format(webapp.__name__))
    host = config['DEFAULT']['HOST']
    port = config['DEFAULT']['PORT']
    debug = config['DEFAULT']['DEBUG']
    app.env = os.environ.get("ENVIRONMENT", config['DEFAULT']['ENVIRONMENT'])

    manager = Manager(app)
    server = Server(host=host, port=port,
                    use_debugger=debug, use_reloader=True)
    manager.add_command("runserver", server)

    manager.run()
