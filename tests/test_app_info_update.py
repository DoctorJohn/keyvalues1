from pathlib import Path

from keyvalues1 import KeyValues1

fixtures = Path("tests/fixtures")


def test_7_days_to_die():
    text = (fixtures / "7-days-to-die.vdf").read_text()
    data = KeyValues1.parse(text)

    assert data["251570"]["common"]["name"] == "7 Days to Die"
    assert data["251570"]["common"]["type"] == "Game"
    assert data["251570"]["common"]["ReleaseState"] == "released"
    assert data["251570"]["common"]["oslist"] == "windows,macos,linux"
    assert data["251570"]["depots"]["branches"]["public"]["buildid"] == "11888660"


def test_ark():
    text = (fixtures / "ark.vdf").read_text()
    data = KeyValues1.parse(text)

    assert data["346110"]["common"]["name"] == "ARK: Survival Evolved"
    assert data["346110"]["common"]["type"] == "Game"
    assert data["346110"]["common"]["ReleaseState"] == "released"
    assert data["346110"]["common"]["oslist"] == "windows,macos"
    assert data["346110"]["depots"]["branches"]["public"]["buildid"] == "12322606"


def test_core_keeper():
    text = (fixtures / "core-keeper.vdf").read_text()
    data = KeyValues1.parse(text)

    assert data["1621690"]["common"]["name"] == "Core Keeper"
    assert data["1621690"]["common"]["type"] == "Game"
    assert data["1621690"]["common"]["ReleaseState"] == "released"
    assert data["1621690"]["common"]["oslist"] == "windows,linux"
    assert data["1621690"]["depots"]["branches"]["public"]["buildid"] == "12411075"


def test_dont_starve_together():
    text = (fixtures / "dont-starve-together.vdf").read_text()
    data = KeyValues1.parse(text)

    assert data["322330"]["common"]["name"] == "Don't Starve Together"
    assert data["322330"]["common"]["type"] == "Game"
    assert data["322330"]["common"]["ReleaseState"] == "released"
    assert data["322330"]["common"]["oslist"] == "windows,macos,linux"
    assert data["322330"]["depots"]["branches"]["public"]["buildid"] == "12326856"


def test_eco():
    text = (fixtures / "eco.vdf").read_text()
    data = KeyValues1.parse(text)

    assert data["382310"]["common"]["name"] == "Eco"
    assert data["382310"]["common"]["type"] == "Game"
    assert data["382310"]["common"]["ReleaseState"] == "released"
    assert data["382310"]["common"]["oslist"] == "windows,macos,linux"
    assert data["382310"]["depots"]["branches"]["public"]["buildid"] == "11262479"


def test_project_zomboid():
    text = (fixtures / "project-zomboid.vdf").read_text()
    data = KeyValues1.parse(text)

    assert data["108600"]["common"]["name"] == "Project Zomboid"
    assert data["108600"]["common"]["type"] == "Game"
    assert data["108600"]["common"]["ReleaseState"] == "released"
    assert data["108600"]["common"]["oslist"] == "windows,macos,linux"
    assert data["108600"]["depots"]["branches"]["public"]["buildid"] == "10105824"


def test_rust():
    text = (fixtures / "rust.vdf").read_text()
    data = KeyValues1.parse(text)

    assert data["252490"]["common"]["name"] == "Rust"
    assert data["252490"]["common"]["type"] == "Game"
    assert data["252490"]["common"]["ReleaseState"] == "released"
    assert data["252490"]["common"]["oslist"] == "windows,macos"
    assert data["252490"]["depots"]["branches"]["public"]["buildid"] == "12395959"


def test_satisfactory():
    text = (fixtures / "satisfactory.vdf").read_text()
    data = KeyValues1.parse(text)

    assert data["526870"]["common"]["name"] == "Satisfactory"
    assert data["526870"]["common"]["type"] == "Game"
    assert data["526870"]["common"]["ReleaseState"] == "released"
    assert data["526870"]["common"]["oslist"] == "windows"
    assert data["526870"]["depots"]["branches"]["public"]["buildid"] == "10115589"


def test_starbound():
    text = (fixtures / "starbound.vdf").read_text()
    data = KeyValues1.parse(text)

    assert data["211820"]["common"]["name"] == "Starbound"
    assert data["211820"]["common"]["type"] == "Game"
    assert data["211820"]["common"]["ReleaseState"] == "released"
    assert data["211820"]["common"]["oslist"] == "windows,macos,linux"
    assert data["211820"]["depots"]["branches"]["public"]["buildid"] == "4369387"


def test_staxel():
    text = (fixtures / "staxel.vdf").read_text()
    data = KeyValues1.parse(text)

    assert data["405710"]["common"]["name"] == "Staxel"
    assert data["405710"]["common"]["type"] == "Game"
    assert data["405710"]["common"]["ReleaseState"] == "released"
    assert data["405710"]["common"]["oslist"] == "windows,macos,linux"
    assert data["405710"]["depots"]["branches"]["public"]["buildid"] == "7473809"


def test_terraria():
    text = (fixtures / "terraria.vdf").read_text()
    data = KeyValues1.parse(text)

    assert data["105600"]["common"]["name"] == "Terraria"
    assert data["105600"]["common"]["type"] == "game"
    assert data["105600"]["common"]["oslist"] == "windows,macos,linux"
    assert data["105600"]["depots"]["branches"]["public"]["buildid"] == "9965506"


def test_tmodloader():
    text = (fixtures / "tmodloader.vdf").read_text()
    data = KeyValues1.parse(text)

    assert data["1281930"]["common"]["name"] == "tModLoader"
    assert data["1281930"]["common"]["type"] == "Game"
    assert data["1281930"]["common"]["ReleaseState"] == "released"
    assert data["1281930"]["common"]["oslist"] == "windows,macos,linux"
    assert data["1281930"]["depots"]["branches"]["public"]["buildid"] == "12408740"


def test_unturned():
    text = (fixtures / "unturned.vdf").read_text()
    data = KeyValues1.parse(text)

    assert data["304930"]["common"]["name"] == "Unturned"
    assert data["304930"]["common"]["type"] == "Game"
    assert data["304930"]["common"]["ReleaseState"] == "released"
    assert data["304930"]["common"]["oslist"] == "windows,macos,linux"
    assert data["304930"]["depots"]["branches"]["public"]["buildid"] == "12446352"


def test_valheim():
    text = (fixtures / "valheim.vdf").read_text()
    data = KeyValues1.parse(text)

    assert data["892970"]["common"]["name"] == "Valheim"
    assert data["892970"]["common"]["type"] == "Game"
    assert data["892970"]["common"]["ReleaseState"] == "released"
    assert data["892970"]["common"]["oslist"] == "windows,linux"
    assert data["892970"]["depots"]["branches"]["public"]["buildid"] == "12413229"
