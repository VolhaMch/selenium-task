import allure
import faker
import pytest

from pathlib import Path

from pages.DemoQA.base_page import DemoQAMainPage


class TestFulfillFormPositive:

    @allure.description('Fulfill the form with valid data')
    def test_fulfill_form(self, demoqa_page, fake_data, random_state_city):
        page = demoqa_page
        state, city = random_state_city
        with allure.step("Fill in first name"):
            page.fill_field(DemoQAMainPage.FIRST_NAME_FIELD, fake_data['first_name'], 'first name')
        with allure.step("Fill in last name"):
            page.fill_field(DemoQAMainPage.LAST_NAME_FIELD, fake_data['last_name'], 'last name')
        with allure.step("Fill in personal email"):
            page.fill_field(DemoQAMainPage.EMAIL_FIELD, fake_data['email'], 'email')
        with allure.step("Choose gender"):
            page.choose_radio(DemoQAMainPage.MALE_RADIO, 'gender')
        with allure.step("Fill in mobile number"):
            page.fill_field(DemoQAMainPage.MOBILE_NUMBER, fake_data['mobile_number'], 'mobile number')
        with allure.step("Scroll down"):
            page.scroll_to_element(DemoQAMainPage.SUBMIT_BUTTON)
        with allure.step("Fill in form 'Subject'"):
            page.fill_field(DemoQAMainPage.SUBJECT_FIELD, fake_data['text'], 'subject')
        with allure.step("Choose hobbies"):
            page.choose_radio(DemoQAMainPage.SPORT_HOBBIES_CHECKBOX, 'hobbies')
        with allure.step("Upload image"):
            file_path = Path(__file__).resolve().parent.parent.parent / "images" / "nikki.png"
            page.choose_file(DemoQAMainPage.CHOOSE_FILE_BUTTON, str(file_path))
        with allure.step("Fill in address"):
            page.fill_field(DemoQAMainPage.CURRENT_ADDRESS_TEXTAREA, fake_data['address'], 'address')
        with allure.step("Scroll down"):
            page.scroll_to_element(DemoQAMainPage.SUBMIT_BUTTON)
        with allure.step("Choose state"):
            page.choose_dropdown_value(DemoQAMainPage.STATE_DROPDOWN, state, 'state')
        with allure.step("Choose city"):
            page.choose_dropdown_value(DemoQAMainPage.CITY_DROPDOWN, city, 'city')
        with allure.step("Click button 'Submit'"):
            page.click_button(DemoQAMainPage.SUBMIT_BUTTON, 'submit')
        with allure.step("Check form iframe appeared"):
            page.check_form_submitted_successfully()


class TestFulfillFormNegative:
    @allure.description('Fulfill the form in invalid email format')
    def test_fulfill_email_invalid_format(self, demoqa_page, invalid_faked_data):
        page = demoqa_page
        with allure.step("Fill in personal email in invalid format"):
            page.fill_field(DemoQAMainPage.EMAIL_FIELD, invalid_faked_data['email'], 'invalid email')
        with allure.step("Scroll down"):
            page.scroll_to_element(DemoQAMainPage.SUBMIT_BUTTON)
        with allure.step("Click button 'Submit'"):
            page.click_button(DemoQAMainPage.SUBMIT_BUTTON, 'Submit')
        with allure.step("Check email field border is red"):
            page.check_field_contains_invalid_value(DemoQAMainPage.EMAIL_FIELD)
        with allure.step("Check form iframe hasn't appeared"):
            page.check_form_not_submitted()

    @pytest.mark.parametrize("invalid_symbols", [('**********'), ('+++++++++'), ('========')])
    @allure.description('Fulfill the form with invalid mobile number')
    def test_fulfill_mobile_number_with_invalid_symbols(self, demoqa_page, invalid_symbols):
        page = demoqa_page
        with allure.step("Scroll down"):
            page.scroll_to_element(DemoQAMainPage.SUBMIT_BUTTON)
        with allure.step("Fill in mobile number with invalid symbols"):
            page.fill_field(DemoQAMainPage.MOBILE_NUMBER, invalid_symbols, 'invalid symbols')
        with allure.step("Scroll down"):
            page.scroll_to_element(DemoQAMainPage.SUBMIT_BUTTON)
        with allure.step("Click button 'Submit'"):
            page.click_button(DemoQAMainPage.SUBMIT_BUTTON, 'Submit')
        with allure.step("Check mobile field  border is red"):
            page.check_field_contains_invalid_value(DemoQAMainPage.MOBILE_NUMBER)
        with allure.step("Check form iframe hasn't appeared"):
            page.check_form_not_submitted()


    @allure.description('Fulfill the form with short mobile number')
    def test_fulfill_short_mobile_number(self, demoqa_page, invalid_faked_data):
        page = demoqa_page
        with allure.step("Scroll down"):
            page.scroll_to_element(DemoQAMainPage.SUBMIT_BUTTON)
        with allure.step("Fill in  mobile number less than 10 numbers"):
            page.fill_field(DemoQAMainPage.MOBILE_NUMBER, invalid_faked_data['mobile_number'], 'short mobile number')
        with allure.step("Scroll down"):
            page.scroll_to_element(DemoQAMainPage.SUBMIT_BUTTON)
        with allure.step("Click button 'Submit'"):
            page.click_button(DemoQAMainPage.SUBMIT_BUTTON, 'Submit')
        with allure.step("Check mobile field border is red"):
            page.check_field_contains_invalid_value(DemoQAMainPage.MOBILE_NUMBER)
        with allure.step("Check form iframe hasn't appeared"):
            page.check_form_not_submitted()


    @allure.description('Leave empty all fialds and click submit')
    def test_leave_empty_all_fields(self, demoqa_page):
        page = demoqa_page
        with allure.step("Scroll down"):
            page.scroll_to_element(DemoQAMainPage.SUBMIT_BUTTON)
        with allure.step("Click button 'Submit'"):
            page.click_button(DemoQAMainPage.SUBMIT_BUTTON, 'Submit')
        with allure.step("Check the following borders are red: first name, last name, mobile, gender"):
            for locator in DemoQAMainPage.REQUIRED_FIELDS:
                page.check_field_contains_invalid_value(locator)
        with allure.step("Check form iframe hasn't appeared"):
            page.check_form_not_submitted()
