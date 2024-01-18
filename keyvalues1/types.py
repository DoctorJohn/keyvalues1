from typing import Dict, List, Tuple, Union

from typing_extensions import TypeAlias

RulePair: TypeAlias = Tuple["RuleString", "RuleValue"]
RuleValue: TypeAlias = Union["RuleString", "RuleDict"]
RuleDict: TypeAlias = List[RulePair]
RuleString: TypeAlias = str

KVPair: TypeAlias = Tuple["KVString", "KVValue"]
KVValue: TypeAlias = Union["KVString", "KVDict"]
KVDict: TypeAlias = Dict["KVString", "KVValue"]
KVString: TypeAlias = str
