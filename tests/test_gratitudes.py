from lib.gratitudes import *

def test_gradtitudes_return_gradtitue():
    test_gradtitude = Gratitudes()
    test_gradtitude.add("life")
    result = test_gradtitude.format()
    
    assert result == "Be grateful for: life"
    
    