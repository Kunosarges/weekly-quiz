from aiohttp import web


class Application(web.Application):
    def __init__(self):
        super().__init__()
        globals()[self.__class__.__name__] = lambda: self

        # Loading handlers
        from quiz.handler import hello


def route(url, name):
    def decorate(handler):
        Application().router.add_route('*', url, handler, name=name)

        return handler

    return decorate
