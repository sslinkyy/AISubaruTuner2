import pytest
from agents.exporter.exporter import apply_changes

import os

def test_apply_changes_importable(tmp_path):
    # apply_changes should be a callable function and not throw when patched stub
    rom = tmp_path / "dummy.bin"
    out = tmp_path / "out.bin"
    rom.write_bytes(b" " * 1024)
    apply_changes(str(rom), [], str(out))
    # If no exception, consider pass
    assert True
