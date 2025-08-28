from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'I am on the loggin page')
def step_impl(context):
    context.browser.get('https://katalon-demo-cura.herokuapp.com/profile.php#login')
    assert(context.browser.title) == "CURA Healthcare Service"

@given(u'I fill my credential')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, 'txt-username')))
    context.browser.find_element(By.ID, 'txt-username').send_keys('John Doe') 
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, 'txt-password')))
    context.browser.find_element(By.ID, 'txt-password').send_keys('ThisIsNotAPassword')

@when(u'I am click Sign in Button')
def step_impl(context):
    context.browser.find_element(By.ID, 'btn-login').click()

@then(u'I Shoud be Logged in')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#appointment>div>div>div>h2"), 'Make Appointment'))
    assert(context.browser.find_element(By.CSS_SELECTOR,"#appointment>div>div>div>h2").text) =="Make Appointment"
    
@given(u'I fill wrong credential')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, 'txt-username')))
    context.browser.find_element(By.ID, 'txt-username').send_keys('John Doe') 
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, 'txt-password')))
    context.browser.find_element(By.ID, 'txt-password').send_keys('ThisIsWrongPassword')

@then(u'I Shoud be Not Logged in and see the error message')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"p.lead.text-danger"), "Login failed! Please ensure the username and password are valid."))
    assert(context.browser.find_element(By.CSS_SELECTOR, "p.lead.text-danger").text) =="Login failed! Please ensure the username and password are valid."