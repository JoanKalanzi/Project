from lib.password_checker import *
import pytest


def test_correct_password_length():
    # Instantiate PasswordChecker with a password argument
    password = PasswordChecker()
    # Call the check method and store the result in a variable
    result = password.check("password")
    # Assert that the result is equal to the original password
    assert result == True


def test_wong_password_length():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check()
        message = str(e.value)
        assert message == "Invalid password, must be 8+ characters."


