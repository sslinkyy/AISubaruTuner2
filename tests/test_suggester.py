import pytest
from agents.suggester.suggester import suggest_changes

def test_suggest_changes_importable():
    # suggest_changes should be a callable function
    assert callable(suggest_changes)
