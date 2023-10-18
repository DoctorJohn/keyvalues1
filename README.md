# KeyValues1

Parser for [version 1 of Valve's KeyValues format](https://developer.valvesoftware.com/wiki/KeyValues).

The focus of this particular library is parsing of relevant `steamcmd` output.

## Installation

```bash
pip install keyvalues1
```

## Usage

```python
from keyvalues1 import KeyValues1

text = """
    "570"
    {
        "common"
        {
            "name" "Dota 2"
            "oslist" "windows,macos,linux"
            "type" "game"
        }
    }
"""

data = KeyValues1.parse(text)

print(data["570"]["common"]["name"])
```
