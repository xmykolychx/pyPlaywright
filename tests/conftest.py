import pytest
from playwright.sync_api import Page
from utils.all_pages import AllPages

@pytest.fixture
def get_page(page: Page):
    def _get_page(page_type):
        page_class = AllPages.PAGE_CLASSES.get(page_type)
        if page_class:
            return page_class(page)
        else:
            raise ValueError(f"Invalid page type: {page_type}")

    return _get_page


@pytest.fixture
def return_pages(get_page):
    def _return_pages(*page_types):
        pages = {}
        for page_type in page_types:
            page = get_page(page_type)
            pages[page_type] = page
        return pages.values()
    return _return_pages
