from src.note_rate import rate_note
import pytest

@pytest.mark.parametrize("note",[0,1,2,3,4,5,6,7,8,9])

def test_rate_note_unsuccessful(note):
   assert  rate_note(note) == "unsuccessful"

@pytest.mark.parametrize("note",[10,11])

def test_rate_note_acceptable(note):
   assert  rate_note(note) == "acceptable"


@pytest.mark.parametrize("note",[12,13])

def test_rate_note_good(note):
   assert  rate_note(note) == "good"

@pytest.mark.parametrize("note",[14,15])

def test_rate_note_very_good(note):
   assert  rate_note(note) == "very good"


@pytest.mark.parametrize("note",[16,17,18,19,20])

def test_rate_note_excellent(note):
   assert  rate_note(note) == "excellent"
