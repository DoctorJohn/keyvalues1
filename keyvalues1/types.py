from typing import Union

from typing_extensions import TypeAlias

KV1Pair: TypeAlias = tuple["KV1String", "KV1Value"]
KV1Value: TypeAlias = Union["KV1String", "KV1Dict"]
KV1Dict: TypeAlias = dict["KV1String", "KV1Value"]
KV1String: TypeAlias = str
