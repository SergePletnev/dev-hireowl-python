import pytest


@pytest.mark.skip
class TestEmployer:
    email_student = 'testemployer@yopmail.com'
    password_student = '123456Qq'

    def test_true(self):
        assert True
