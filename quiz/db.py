import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql
from aiopg.sa import create_engine

from quiz.util import options


options.define('db_user', default='quiz',
               help='Database username.')
options.define('db_database', default='quiz',
               help='Database password.')
options.define('db_pass', default='quiz',
               help='Database name.')
options.define('db_host', default='127.0.0.1',
               help='Database host.')


Base = declarative_base()

Integer, String = sa.Integer, sa.String
JSON = postgresql.JSON
JSONB = postgresql.JSONB
Column = sa.Column

_engine = create_engine(user=options.options.db_user,
                        database=options.options.db_database,
                        host=options.options.db_host,
                        password=options.options.db_pass)

async def acquire():
    return (await _engine).acquire()
