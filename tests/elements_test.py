import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            # обьявляем и присваеваем результат с входными данными
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_perma_address = text_box_page.check_field_form()
            print(output_name)
            assert full_name == output_name, 'error name'
            assert email == output_email, 'error email'
            assert current_address == output_current_address, 'error current_address'
            assert permanent_address == output_perma_address, "error permanent_address"
            # time.sleep(5)

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_check_box = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            # print(input_check_box)
            # print(output_result)
            assert input_check_box == output_result, 'выбранные чекпоинты не соответствуют результату'

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            # radio_button_page.click_on_the_radio_button('no')
            # output_no = radio_button_page.get_output_result()

            assert output_yes == "Yes", "Yes, have not been selected"
            assert output_impressive == "Impressive", "Impressive, have not been selected"
            # assert output_no == "No", "No, have not been selected"

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result, "результат таблицы не совпадает в введенным результатом"
            # time.sleep(1)

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0,5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            # print(key_word)
            # print(table_result)
            assert key_word in table_result, "результат поиска не совпадает с запросом "


