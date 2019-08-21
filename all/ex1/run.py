import os
import webapp
from webapp import app
from webapp.utils import get_configurations


if __name__ == "__main__":
    config = get_configurations("{0}.cfg".format(webapp.__name__))
    host = config['DEFAULT']['HOST']
    port = config['DEFAULT']['PORT']
    debug = config['DEFAULT']['DEBUG']
    app.env = os.environ.get("ENVIRONMENT", config['DEFAULT']['ENVIRONMENT'])

    app.run(host, port, debug=debug)
