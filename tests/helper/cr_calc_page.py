from tests.helper.base_app import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class cr_calc_locators:
    LOCATOR_SUBMIT = (By.NAME, "id_submit_calc")
    LOCATOR_ERROR = (By.CLASS_NAME, "errorlist")

class CommonHelper(BasePage):

    def enter_input(self, type, digit):
        input_field = self.find_element((By.CSS_SELECTOR, type), time=5)
        input_field.click()
        input_field.send_keys(digit)
        return input_field

    def click_submit_button(self):
        return self.find_element(cr_calc_locators.LOCATOR_SUBMIT,time=2).click()
    
    def check_error_forms(self):
        error_list = self.find_elements(cr_calc_locators.LOCATOR_ERROR, time=2)
        if (error_list):
            return error_list
        else:
            return None

    def set_select_option(self, id, value):
        select = Select(self.find_element((By.CSS_SELECTOR, id), time=5))
        # select by value 
        select.select_by_value(value)

    def get_value(self, id):
        el = self.find_element((By.ID, id),time=2)
        return el.text