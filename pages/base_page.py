from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Тут методы которые облегчают работу со страницами"""
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        # жди 10 секунд пока локатор не будет представлен
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        # жди 10 секунд пока все элементы не будут представлен
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        # найти элемент и взять текст из дом дерева(не обязательно чтобы был виден)
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=5):
        # найти элементы и взять текст из дом дерева(не обязательно чтобы был виден)
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        # использование элемента который не виден
        return Wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        # кликабельный
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        # перемещать нас к нужному элементу
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
