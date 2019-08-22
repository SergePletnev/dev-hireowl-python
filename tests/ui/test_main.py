import pytest


class TestHomePageContent:

    def test_user_should_see_popular_jobs(self, home_page):
        elements = home_page.get_popular_jobs()
        assert len(elements) == 8

    @pytest.mark.skip(reason='just for check')
    def test_terms_of_use_valid(self, browser, home_page):
        terms_of_use_page = home_page.navigate_to_terms_of_use()
        assert True

    @pytest.mark.skip(reason='just for check')
    def test_page_should_have_correct_title(self, home_page):
        assert home_page.get_page_title() == 'HireOwl: Connecting Businesses to University Students'

    @pytest.mark.skip(reason='just for check')
    def test_guest_should_see_hottest_jobs(self):
        assert True

    @pytest.mark.skip(reason='just for check')
    def test_guest_should_see_trending_students(self):
        assert True
