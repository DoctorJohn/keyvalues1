from keyvalues1 import KeyValues1

text = """
    "570"
    {
        "common"
        {
            "name" "Dota 2"
            "oslist" "windows,macos,linux"
            "type" "Game"
        }
    }
"""

data = KeyValues1.parse(text)

assert isinstance(data["570"], dict)
assert isinstance(data["570"]["common"], dict)

assert data["570"]["common"]["name"] == "Dota 2"
assert data["570"]["common"]["type"] == "Game"
assert data["570"]["common"]["oslist"] == "windows,macos,linux"
