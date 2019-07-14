import os

from flask_script import Manager, Server
import webapp
from webapp import app
from webapp.utils import get_configurations


if __name__ == "__main__":
    config = get_configurations("{0}.cfg".format(webapp.__name__))
    host = config['DEFAULT']['HOST']
    port = config['DEFAULT']['PORT']
    debug = True if config['DEFAULT']['DEBUG'] == "True" else False
    app.env = os.environ.get("ENVIRONMENT", config['DEFAULT']['ENVIRONMENT'])

    manager = Manager(app)
    server = Server(host=host, port=port,
                    use_debugger=debug, use_reloader=True)
    manager.add_command("runserver", server)

    host_1 = config['PRODUCTION']['HOST']
    port_1 = config['PRODUCTION']['PORT']
    debug_1 = True if config['PRODUCTION']['DEBUG'] == "True" else False
    app.env = os.environ.get("ENVIRONMENT", config['PRODUCTION']['ENVIRONMENT'])
    server_1 = Server(host=host_1, port=port_1,
                    use_debugger=debug_1, use_reloader=True)
    manager.add_command("start", server_1)

    manager.run()
