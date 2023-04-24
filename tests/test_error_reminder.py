# File: tests/test_reminder.py

from lib.error_reminder import *


# Pass test as task was set

def test_reminder():
    reminder = Reminder("Kay")
    result = reminder.remind()
    assert result == "walk, Kay!"





