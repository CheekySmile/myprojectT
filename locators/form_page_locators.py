import random

from selenium.webdriver.common.by import By


class TextFormPageLocators:
    #form
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    GENDER = (By.CSS_SELECTOR, f"div[class*='custom-control'] input[id='gender-radio-{random.randint(1,3)}']")
    MOBILE = (By.CSS_SELECTOR, "input[id='userNumber']")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    SUBJECTS = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    HOBBIES = (By.CSS_SELECTOR, f"div[class*='custom-control'] input[id='hobbies-checkbox-{random.randint(1,3)}']")
    FILE_INPUT = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    SELECT_STATE = (By.CSS_SELECTOR, "div[id='state']")
    STATE_INPUT = (By.CSS_SELECTOR, "input[id='react-select-8-input']")
    SELECT_CITY = (By.CSS_SELECTOR, "div[id='city']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[id='react-select-9-input']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    #results
    #RESULT_TABLE =

