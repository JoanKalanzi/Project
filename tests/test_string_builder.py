from lib.string_builder import *

def test_string_builder():
    str_builder = StringBuilder()
    str_builder.add("testing")
    str_builder.size()
    result = str_builder.output()
    
    assert result == "testing"
