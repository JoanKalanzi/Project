from lib.present import *
import pytest

def presents_returns_none():
    present = Present()
    present.wrap("car")
    assert present.unwrap()== "car"


    #if we unwrap before wrapping the present

def test_unwrap_without_wrapping():
        present = Present()
        with pytest.raises(Exception) as e:
          present.unwrap()
        message = str(e.value)
        assert message == "No contents have been wrapped."
