from quiz.handler import base
from quiz import app


@app.route('/', 'hello')
class Hello(base.Handler):
    @base.get_args
    async def get(self, name):
        await self.render('hello.html', name=name)


@app.route('/quiz', 'quiz')
class Hello(base.Handler):
    @base.get_args
    async def get(self, quiz_id):
        # @todo 处理一下读第几次quiz的问题
        if False:
            await self.render('notlogin.html')
        else:
            questions = {'q1': [], 'q2': ['a', 'b', 'c', 'd']}
            await self.render('quiz.html', questions=questions)


@app.route('/commit', 'commit')
class Hello(base.Handler):
    @base.post_args
    async def post(self, choice, user):

        self.response.text='success'
