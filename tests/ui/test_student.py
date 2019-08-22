import pytest


@pytest.mark.skip
@pytest.mark.usefixtures("student")
class TestStudent:
    email_student = 'teststudent@yopmail.com'
    password_student = '123456Qq'

    def test_true(self):
        assert True

    def test_false(self):
        assert False
