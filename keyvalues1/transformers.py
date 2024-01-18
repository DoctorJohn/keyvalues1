from typing import List

from lark import Token, Transformer

from keyvalues1.types import KVPair, RuleDict, RulePair, RuleString, RuleValue


class TreeToJson(Transformer[Token, KVPair]):
    def pair(self, items: RulePair):
        key, value = items
        return key, value

    def value(self, items: List[RuleValue]):
        item = items[0]

        if isinstance(item, list):
            return dict(item)

        return item

    def dict(self, items: RuleDict):
        return dict(items)

    def string(self, items: List[RuleString]):
        return items[0].strip('"')
