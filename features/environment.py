from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def before_scenario(context,scenario):
  option = Options()
  option.add_argument("disable-gpu")
  if os.getenv("HEADLESS") =='true':
    option.add_argument("headless")
    
  context.browser = webdriver.Chrome()
  context.browser.maximize_window()

def after_scenario(context, scenario):
  context.browser.quit()
