from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def before_scenario(context,scenario):
  option = Options()
  option.add_argument("--disable-gpu")
  option.add_argument("--no-sandbox")
  option.add_argument("--disable-dev-shm-usage")
  if os.getenv("HEADLESS") =='true':
    option.add_argument("--headless")

  context.browser = webdriver.Chrome(options=options)
  context.browser.maximize_window()

def after_scenario(context, scenario):
  context.browser.quit()
