import pytest
from agents.parser.parser import parse_rom

def test_parse_rom_importable():
    # parse_rom should be a callable function
    assert callable(parse_rom)
