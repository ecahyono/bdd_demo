import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)


@given(u'I am on the login page')
def navigate_to_login_page(context):
    """
    Navigate to the login page.
    """
    logger.info("Navigating to the login page")
    context.browser.get('https://katalon-demo-cura.herokuapp.com/profile.php#login')
    assert context.browser.title == "CURA Healthcare Service"
    logger.info("Successfully navigated to login page")


@given(u'I fill my credential')
def fill_correct_credentials(context):
    """
    Fill in the correct username and password.
    """
    logger.info("Filling in correct credentials")
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, 'txt-username')))
    context.browser.find_element(By.ID, 'txt-username').send_keys('John Doe')
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, 'txt-password')))
    context.browser.find_element(By.ID, 'txt-password').send_keys('ThisIsNotAPassword')
    logger.info("Credentials filled successfully")


@when(u'I click Sign in Button')
def click_sign_in_button(context):
    """
    Click the Sign in button.
    """
    logger.info("Clicking the Sign in button")
    context.browser.find_element(By.ID, 'btn-login').click()
    logger.info("Sign in button clicked")


@then(u'I Should be Logged in')
def verify_logged_in(context):
    """
    Verify that the user is logged in by checking for the 'Make Appointment' text.
    """
    logger.info("Verifying successful login")
    WebDriverWait(context.browser, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#appointment>div>div>div>h2"), 'Make Appointment')
    )
    assert context.browser.find_element(By.CSS_SELECTOR, "#appointment>div>div>div>h2").text == "Make Appointment"
    logger.info("Login verification successful")


@given(u'I fill wrong credential')
def fill_wrong_credentials(context):
    """
    Fill in the wrong username and password.
    """
    logger.info("Filling in wrong credentials")
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, 'txt-username')))
    context.browser.find_element(By.ID, 'txt-username').send_keys('John Doe')
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, 'txt-password')))
    context.browser.find_element(By.ID, 'txt-password').send_keys('ThisIsWrongPassword')
    logger.info("Wrong credentials filled")


@then(u'I Should be Not Logged in and see the error message')
def verify_login_failed(context):
    """
    Verify that the login failed and the error message is displayed.
    """
    logger.info("Verifying login failure")
    WebDriverWait(context.browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "p.lead.text-danger"),
            "Login failed! Please ensure the username and password are valid."
        )
    )
    assert context.browser.find_element(By.CSS_SELECTOR, "p.lead.text-danger").text == \
            "Login failed! Please ensure the username and password are valid."
    logger.info("Login failure verification successful")
