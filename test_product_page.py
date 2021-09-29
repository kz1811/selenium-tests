import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import time

@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_the_prices_of_the_basket_and_the_item_should_be_the_same()
    page.check_the_names_of_the_item_and_the_alert_should_be_the_same()

@pytest.mark.skip
def test_guest_can_add_product_to_basket_2(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    #page.check_the_prices_of_the_basket_and_the_item_should_be_the_same()
    #page.check_the_names_of_the_item_and_the_alert_should_be_the_same()

@pytest.mark.skip
@pytest.mark.xfail
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    #Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
    #Добавляем товар в корзину
    page.add_to_basket()
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()

@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):
    #Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()

@pytest.mark.skip
@pytest.mark.xfail
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    #Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
    #Добавляем товар в корзину
    page.add_to_basket()
    #Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.should_dissapear_of_success_message()

def test_guest_should_see_login_link_on_roduct_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
