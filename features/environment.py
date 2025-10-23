"""
Environment setup for Behave tests using Selenium WebDriver.
"""

import logging
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configure logging to output to file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('test_execution.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def before_scenario(context, scenario):
    """
    Set up the browser before each scenario.
    """
    logger.info(f"Starting scenario: {scenario.name}")
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
        logger.info("Browser initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing browser: {e}")
        print(f"Error initializing browser: {e}")
        raise


def after_scenario(context, scenario):
    """
    Clean up the browser after each scenario.
    """
    logger.info(f"Ending scenario: {scenario.name}")
    print("Running after_scenario")
    if hasattr(context, 'browser'):
        try:
            context.browser.quit()
            print("Browser closed successfully")
            logger.info("Browser closed successfully")
        except Exception as e:
            logger.error(f"Error closing browser: {e}")
            print(f"Error closing browser: {e}")
    else:
        logger.warning("No browser instance found in context")
        print("No browser instance found in context")
