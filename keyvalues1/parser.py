from lark import Lark
from keyvalues1.transformers import TreeToJson


class KeyValues1:
    grammar = """
    pair: string value
    value: string | dict
    dict: "{" (pair)* "}"
    string: ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.CPP_COMMENT
    %import common.WS
    %ignore CPP_COMMENT
    %ignore WS
    """

    parser = Lark(grammar, start="pair")

    transformer = TreeToJson()

    @classmethod
    def parse(cls, raw_steam_app_info: str) -> dict:
        tree = cls.parser.parse(raw_steam_app_info)
        return dict([cls.transformer.transform(tree)])
