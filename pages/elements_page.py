import random
import allure
from utilities.logger import Logger
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        """Шаги для заполнения полей"""
        with allure.step('Fill all fields'):
            Logger.add_start_step(method='fill_all_fields')
            person_info = next(generated_person())
            full_name = person_info.full_name
            email = person_info.email
            current_address = person_info.current_address
            permanent_address = person_info.permanent_address
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
            self.element_is_visible(self.locators.SUBMIT).click()
            Logger.add_end_step(self.driver.current_url, method='fill_all_fields')
            return full_name, email, current_address, permanent_address

    def check_field_form(self):
        """Вытянуть текст со страницы для дальнейшей проверки"""
        with allure.step('Check field form'):
            Logger.add_start_step(method='check_field_form')
            full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
            email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
            current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
            permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
            Logger.add_end_step(self.driver.current_url, method='check_field_form')
            return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    """Работа с чек-боксами"""
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        with allure.step('Open full list'):
            Logger.add_start_step(method='open_full_list')
            self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()
            Logger.add_end_step(self.driver.current_url, method='open_full_list')

    def click_random_checkbox(self):
        """Положить в список все элементы"""
        with allure.step('Click random checkbox'):
            Logger.add_start_step(method='click_random_checkbox')
            item_list = self.elements_are_visible(self.locators.ITEM_LIST)
            count = 21
            while count != 0:
                item = item_list[random.randint(1, 15)]
                if count > 0:
                    self.go_to_element(item)
                    item.click()
                    count -= 1
                else:
                    break
            Logger.add_end_step(self.driver.current_url, method='click_random_checkbox')

            # time.sleep(2)

    def get_checked_checkboxes(self):
        """После того как отметили чек бокс будем ходить и проверять отмеченные и добавлять в список"""
        with allure.step('Get checked checkboxes'):
            Logger.add_start_step(method='get_checked_checkboxes')
            checked_list = self.element_are_present(self.locators.CHECKED_ITEMS)
            data = []
            for box in checked_list:
                title_item = box.find_element("xpath", self.locators.TITLE_ITEM)
                data.append(title_item.text)
            Logger.add_end_step(self.driver.current_url, method='get_checked_checkboxes')
            return str(data).replace(' ', '').replace('.doc', '').replace('.', '').lower()

    def get_output_result(self):
        with allure.step('Get output result'):
            Logger.add_start_step(method='get_output_result')
            result_list = self.element_are_present(self.locators.OUTPUT_RESULT)
            data = []
            for item in result_list:
                data.append(item.text)
            Logger.add_end_step(self.driver.current_url, method='get_output_result')
            return str(data).replace(' ', '').replace('.doc', '').replace('.', '').lower()


class RadioButtonPage(BasePage):
    """Работа с радио-батон"""
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        with allure.step('Click on the radio button'):
            Logger.add_start_step(method='click_on_the_radio_button')
            choices = {'yes': self.locators.YES_RADIOBUTTON,
                       'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                       'no': self.locators.NO_RADIOBUTTON
                       }
            radio = self.element_is_visible(choices[choice]).click()
            Logger.add_end_step(self.driver.current_url, method='click_on_the_radio_button')

    def get_output_result(self):
        with allure.step('Get output result'):
            Logger.add_start_step(method='get_output_result')

            Logger.add_end_step(self.driver.current_url, method='get_output_result')
            return self.element_is_present(self.locators.OUTPUT_RADIOBUTTON).text


class WebTablePage(BasePage):
    """Работа с таблицей"""
    locators = WebTablePageLocators()

    def add_new_person(self, count=1):
        """Заполнение таблицы"""
        with allure.step('Add new person'):
            Logger.add_start_step(method='add_new_person')
            i = 0
            while i < count:
                person_info = next(generated_person())
                firstname = person_info.firstname
                lastname = person_info.lastname
                email = person_info.email
                age = person_info.age
                salary = person_info.salary
                department = person_info.department
                self.element_is_visible(self.locators.ADD_BUTTON).click()
                self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
                self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
                self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
                self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
                self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
                self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
                self.element_is_visible(self.locators.SUBMIT).click()
                i += 1
                Logger.add_end_step(self.driver.current_url, method='add_new_person')
                return [firstname, lastname, str(age), email, str(salary), department]

    def check_new_added_person(self):
        with allure.step('Check new added person'):
            Logger.add_start_step(method='check_new_added_person')
            person_list = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
            data = []
            for item in person_list:
                data.append(item.text.splitlines())
            Logger.add_end_step(self.driver.current_url, method='check_new_added_person')
            return data

    def search_some_person(self, key_word):
        with allure.step('Search some person'):
            Logger.add_start_step(method='search_some_person')
            self.element_is_visible(self.locators.INPUT_SEARCH).send_keys(key_word)
            Logger.add_end_step(self.driver.current_url, method='search_some_person')

    def check_search_person(self):
        with allure.step('Сheck search person'):
            Logger.add_start_step(method='check_search_person')
            delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
            row = delete_button.find_element("xpath", self.locators.ROW_PARENT)
            Logger.add_end_step(self.driver.current_url, method='check_search_person')
            return row.text.splitlines()
