import pytest
import home_page
from unittest import mock
#run with -v -s enabled


def test_outputReading(capfd):
    home_page.homePage()
    stdout, stderr = capfd.readouterr()
    assert stdout == "Welcome to InCollege!\n"
