# KeyValues1

[![PyPI][pypi-image]][pypi-url]
![PyPI - Python Version][python-image]
[![Codecov][codecov-image]][codecov-url]
[![License][license-image]][license-url]

[pypi-image]: https://img.shields.io/pypi/v/keyvalues1
[pypi-url]: https://pypi.org/project/keyvalues1/
[python-image]: https://img.shields.io/pypi/pyversions/keyvalues1
[codecov-image]: https://codecov.io/gh/DoctorJohn/keyvalues1/branch/main/graph/badge.svg
[codecov-url]: https://codecov.io/gh/DoctorJohn/keyvalues1
[license-image]: https://img.shields.io/pypi/l/keyvalues1
[license-url]: https://github.com/DoctorJohn/keyvalues1/blob/master/LICENSE

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
