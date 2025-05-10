from typing import List

from lark import Token, Transformer

from keyvalues1.types import KV1Dict, KV1Pair, KV1String, KV1Value


class TreeToJson(Transformer[Token, KV1Pair]):
    def pair(self, items: KV1Pair) -> KV1Pair:
        return items

    def value(self, items: List[KV1Value]) -> KV1Value:
        return items[0]

    def dict(self, items: List[KV1Pair]) -> KV1Dict:
        return dict(items)

    def string(self, items: List[str]) -> KV1String:
        return items[0].strip('"')
