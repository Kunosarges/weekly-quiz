from quiz import db


class Session(db.Base):
    __tablename__ = 'session'

    sid = db.Column(db.String, primary_key=True)
    uid = db.Column(db.Integer)
    extra_data = db.Column(db.JSONB)


table = Session.__table__


async def get(sid):
    async with await db.acquire() as conn:
        result = await conn.execute(table.select().where(table.c.sid == sid))
        sess = await result.fetchone()
        print(sess)
        return sess
