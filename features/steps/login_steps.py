from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'I am on the loggin page')
def step_impl(context):
    context.browser.get('https://frontend-lelang.lelang.dev.torche.id/login')
    assert(context.browser.title) == "Lelang Indonesia | DJKN"

@given(u'I fill my credential')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    context.browser.find_element(By.ID, 'username').send_keys('secondacount507@gmail.com') 
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    context.browser.find_element(By.ID, 'password').send_keys('Rahasi@123')

@when(u'I am click Sign in Button')
def step_impl(context):
    context.browser.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/main/div[1]/div[2]/div/form/button').click()

@then(u'I Shoud be Logged in')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"h3.text-xl"), 'Kategori Objek Lelang'))
    assert(context.browser.find_element(By.CSS_SELECTOR,"h3.text-xl").text) =="Kategori Objek Lelang"
    
@given(u'I fill wrong credential')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    context.browser.find_element(By.ID, 'username').send_keys('salah507@gmail.com') 
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    context.browser.find_element(By.ID, 'password').send_keys('salah@123')

@then(u'I Shoud be Not Logged in and see the error message')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"span.text-center"), "Login gagal!"))
    assert(context.browser.find_element(By.CSS_SELECTOR, "span.text-center.text-xl.font-bold.text-primary-500").text) =="Login gagal!"
    assert(context.browser.find_element(By.CSS_SELECTOR, "span.text-center.text-sm.font-light.text-ternary-gray-200").text) =="Kredensial tidak valid."
