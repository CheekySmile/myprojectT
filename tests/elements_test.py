import pathlib
import random
import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):  # проверяем текстбокс
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_addr, "the current address does not match"
            assert permanent_address == output_per_addr, "the permanent does not match"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, "checkboxes have not been selected"

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == 'No', "'No' have not been selected"

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            check_person = web_table_page.check_new_person()
            assert new_person in check_person, "Person does not exist"

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            keyword = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_person(keyword)
            table_result = web_table_page.check_search_person()
            assert keyword in table_result, "Person not found"

        def test_web_table_update_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            keyword = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_person(keyword)
            update_person = web_table_page.update_person_info()[random.randint(0, 5)]
            web_table_page.search_person(update_person)
            row = web_table_page.check_search_person()
            assert update_person in row, "The person card has not been changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            keyword = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_person(keyword)
            web_table_page.delete_person()
            text = web_table_page.check_delete_person()
            assert text == "No rows found", "Person has not been deleted"

        def test_web_table_change_count_rows(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            counts = web_table_page.change_some_rows()
            assert counts == [5, 10, 20, 25, 50, 100], "The number of rows has not been changed or changed incorrectly"

    class TestButtonsPage:
        def test_different_click_on_the_buttons(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            double = buttons_page.click_on_different_buttons('double')
            right = buttons_page.click_on_different_buttons('right')
            click = buttons_page.click_on_different_buttons('click')
            assert double == "You have done a double click", "The double button was not pressed"
            assert right == "You have done a right click", "The right button was not pressed"
            assert click == "You have done a dynamic click", "The click button was not pressed"

    class TestLinksPage:
        def test_check_links(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "the link is broken or url is incorrect"

        def test_check_dynamic_links(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_dynamic_link()
            assert href_link == current_url, "the link is broken or url is incorrect"

        def test_broken_links(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_links('https://demoqa.com/bad-request')
            assert response_code == 400, "the link is correct or response code is not 400"
            response_code = links_page.check_broken_links('https://demoqa.com/forbidden')
            assert response_code == 403, "the link is correct or response code is not 403"
            response_code = links_page.check_broken_links('https://demoqa.com/invalid-url')
            assert response_code == 404, "the link is correct or response code is not 404"

    class TestUploadAndDownload:
        def test_upload_file(self, driver):
            upload_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_page.open()
            base_dir, text = upload_page.upload_file()
            assert base_dir == text, "the file has not been uploaded"

        def test_download_file(self, driver):
            upload_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_page.open()
            check = upload_page.download_file()
            assert check is True, "the file has not been downloaded"
