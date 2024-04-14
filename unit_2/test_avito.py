import pytest
from playwright.sync_api import Page, expect

LOCATOR = '.desktop-impact-item-eeQO3'
URL_AVITO = 'https://www.avito.ru/avito-care/eco-impact'
PATH_SCREEN = 'output/'


@pytest.fixture(autouse=True)
def before_each_page_goto(page: Page):
    page.goto(URL_AVITO)


def test_atmosphere_id_one(page: Page):
    child = page.get_by_text('не попало в атмосферу')
    locator = page.locator(LOCATOR).filter(has=child)
    expect(locator).to_be_visible()
    locator.screenshot(path=f'{PATH_SCREEN}ID1.png')


def test_water_id_two(page: Page):
    child = page.get_by_text('было сохранено')
    locator = page.locator(LOCATOR).filter(has=child)
    expect(locator).to_be_visible()
    locator.screenshot(path=f'{PATH_SCREEN}ID2.png')


def test_energy_id_three(page: Page):
    child = page.get_by_text('было сэкономлено')
    locator = page.locator(LOCATOR).filter(has=child)
    expect(locator).to_be_visible()
    locator.screenshot(path=f'{PATH_SCREEN}ID3.png')
