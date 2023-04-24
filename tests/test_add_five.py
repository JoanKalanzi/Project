from lib.add_five import *  #  step 1 -> import the function your trying test
def test_add_five_returns_eight_for_three(): # step 2 - create a function example, it must start with keyword TEST_ and the rest should describe what the test verifies
  result = add_five(3)
  # we run the function with the argument 3
  assert result == 8
  # the assert describe that this function should return 8
