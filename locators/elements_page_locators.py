from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # Описываем элементы которые находятся на тестируемой страничке
    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # creation form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title = 'Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class = 'rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class = 'rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class = 'text-success']")


class RadioButtonPageLocators:
    YES_RBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    NO_RBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    IMPRESSIVE_RBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class = 'text-success']")


class WebTablePageLocators:
    #add new person
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    #tables
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    NO_ROWS = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROWS = (By.CSS_SELECTOR, "select[aria-label='rows per page']")

    #update person
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    UPDATE_FIRSTNAME = (By.CSS_SELECTOR, "input[id='firstName']")
    UPDATE_LASTNAME = (By.CSS_SELECTOR, "input[id='lastName']")
    UPDATE_EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    UPDATE_AGE = (By.CSS_SELECTOR, "input[id='age']")
    UPDATE_SALARY = (By.CSS_SELECTOR, "input[id='salary']")
    UPDATE_DEPARTMENT = (By.CSS_SELECTOR, "input[id='department']")
    UPDATE_SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")


