from lib.check_codeword import *

def test_check_codeword() :
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_wong():
    result = check_codeword("Joan")
    assert result == "WRONG!"

def test_check_close():
  result = check_codeword("house")
  assert result == "Close, but nope."
