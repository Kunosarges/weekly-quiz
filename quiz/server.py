from aiohttp import web
from quiz.util import options

from quiz import app

options.define('port', default='8888',
               help='Server listening port.')
options.define('host', default='127.0.0.1',
               help='Server listening host.')
options.define('env', default='development',
               help='Setup the running environment')

if __name__ == '__main__':
    host = options.options.host
    port = options.options.port
    web.run_app(app=app.Application(),
                host=host,
                port=port)
