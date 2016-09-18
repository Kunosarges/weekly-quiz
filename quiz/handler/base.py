import asyncio
from aiohttp import web

from quiz import template
from quiz.model import session


class Handler(web.View):
    @asyncio.coroutine
    def __iter__(self, *args, **kwargs):
        self.response = web.Response()
        yield from self.prepare()
        yield from super(Handler, self).__iter__()

        return self.response

    async def prepare(self):
        self.session = await self.update_session()
        pass

    async def update_session(self, drop=False, **kwargs):
        sid = self.request.cookies.get('sid')

        if not (sid or kwargs):
            sess = {}
        elif sid:
            sess = session.get(sid)

            if (drop):
                session.drop(sid)
                self.response.del_cookie('sid')

            if not sess:
                self.response.del_cookie('sid')
        else:
            sid, sess = session.create(**kwargs)
            self.response.set_cookie('sid', sid)

        return sess

    async def render(self, template_name, **kwargs):
        self.response.content_type = 'text/html'
        tmpl = template.Environment().get_template(template_name)
        self.response.text = tmpl.render(kwargs)


def authenticate():
    def decorate(func):
        async def wrapped(self, *args, **kwargs):
            sess = self.session()
            if not sess:
                # custom error
                raise web.HTTPUnauthorized()

            self.sess = session
            return func(self, *args, **kwargs)

        return wrapped

    return decorate


def route_args(func):
    def wrapped(self, **kwargs):
        return func(self, **{kwargs, self.request.match_info})

    return wrapped


def get_args(func):
    def wrapped(self, **kwargs):
        return func(self, **{kwargs, self.request.GET})

    return wrapped


def post_args(coroutine):
    async def wrapped(self, **kwargs):
        return await coroutine(self, **{kwargs, await self.request.post()})

    return wrapped
