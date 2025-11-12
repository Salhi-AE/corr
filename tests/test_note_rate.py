from src.note_rate import rate_note
import pytest

@pytest.mark.parametrize("note",[0,1,2,3,4,5,6,7,8,9])

def test_rate_note_unsuccessful(note):
   assert  rate_note(note) == "unsuccessful"

def test_rate_10_returns_acceptable():
    assert rate_note(10) == "acceptable"

def test_rate_12_returns_good():
    assert rate_note(12) == "good"