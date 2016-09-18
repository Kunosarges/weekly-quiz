from os import path
import jinja2


class Undefined(jinja2.runtime.Undefined):
    def __getitem__(self, _):
        return self


class Environment(jinja2.Environment):
    def __init__(self):
        super(Environment, self).__init__(
            loader=jinja2.FileSystemLoader(path.join(
                path.dirname(__file__), 'ui/templates')),
            autoescape=True,
            trim_blocks=True,
            undefined=Undefined)
        self.globals['len'] = len
        self.globals['chr'] = chr

        globals()[self.__class__.__name__] = lambda: self
