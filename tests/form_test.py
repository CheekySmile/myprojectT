from pages.form_page import TextFormPage


class TestForm:
    class TestFormPage:
        def test_form(self, driver):
            text_form_page = TextFormPage(driver, 'https://demoqa.com/automation-practice-form')
            text_form_page.open()