from typing import TypeAlias, Union

KV1Pair: TypeAlias = tuple["KV1String", "KV1Value"]
KV1Value: TypeAlias = Union["KV1String", "KV1Dict"]
KV1Dict: TypeAlias = dict["KV1String", "KV1Value"]
KV1String: TypeAlias = str
