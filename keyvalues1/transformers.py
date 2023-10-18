from lark import Transformer


class TreeToJson(Transformer):
    def pair(self, items):
        key, value = items
        return key, value

    def value(self, items):
        return items[0]

    def dict(self, items):
        return dict(items)

    def string(self, items):
        return items[0].strip('"')
