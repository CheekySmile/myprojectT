from generator.generator import generated_person, generated_file
from locators.form_page_locators import TextFormPageLocators
from pages.base_page import BasePage


class TextFormPage(BasePage):
    locators = TextFormPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        base_dir = generated_file()
