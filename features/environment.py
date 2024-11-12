from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def before_scenario(context, scenario):
  print("Running before_scenario")
  options = Options()
  options.add_argument("--disable-gpu")
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  if os.getenv("HEADLESS") == 'true':
      options.add_argument("--headless")

  try:
    context.browser = webdriver.Chrome(options=options)
    context.browser.maximize_window()
    print("Browser initialized successfully")
  except Exception as e:
    print(f"Error initializing browser: {e}")
    raise

def after_scenario(context, scenario):
  print("Running after_scenario")
  if hasattr(context, 'browser'):
    try:
        context.browser.quit()
        print("Browser closed successfully")
    except Exception as e:
        print(f"Error closing browser: {e}")
  else:
    print("No browser instance found in context")
