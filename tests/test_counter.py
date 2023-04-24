from lib.counter import *

def test_counter_return_count():
    counting = Counter()
    counting.add(5)
    result = counting.report()
    
    assert result == "Counted to 5 so far."