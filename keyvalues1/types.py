from typing import Dict, Tuple, Union

from typing_extensions import TypeAlias

KV1Pair: TypeAlias = Tuple["KV1String", "KV1Value"]
KV1Value: TypeAlias = Union["KV1String", "KV1Dict"]
KV1Dict: TypeAlias = Dict["KV1String", "KV1Value"]
KV1String: TypeAlias = str
