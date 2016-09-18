from quiz.handler import base
from quiz import app


@app.route('/', 'hello')
class Hello(base.Handler):
    @base.get_args
    async def get(self, name):
        await self.render('hello.html', name=name)
