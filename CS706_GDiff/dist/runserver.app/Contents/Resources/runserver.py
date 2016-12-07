from StructOpt import app;
import sys

import jinja2
template_dir = '/StructOpt/templates'
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)

# Launching our server
if __name__ == '__main__':
    import os
    #HOST = os.environ.get('SERVER_HOST', '128.104.200.106')
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
    

    
 