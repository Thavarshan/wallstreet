"""Small starter test so you can check your Python setup."""

from wallstreet import __version__


def test_package_has_version() -> None:
    assert __version__ == "0.1.0"
