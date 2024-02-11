import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    parser = argparse.ArgumentParser(description="Update apt-cacher-ng")
    parser.add_argument("--url", required=True, help="URL of the proxy")
    parser.add_argument("--browserless", required=True, help="URL of browserless")

    args = parser.parse_args()

    url_argument = args.url
    browserless_argument = args.browserless
    
    driver = create_con(browserless_argument)
    try: 
        driver.get(f"{url_argument}/acng-report.html")
        click(driver, "doImport")
        driver.quit()
    except:
        driver.quit()
        driver = None
        driver = create_con(browserless_argument)
        driver.get(f"{url_argument}/acng-report.html")
        click(driver, "doImport")
        driver.quit()
    
    time.sleep(5)
    
    driver = create_con(browserless_argument)
    driver.get(f"{url_argument}/acng-report.html")
    click(driver, "doDownload")
    click(driver, "doMirror")
    driver.quit()

def create_con(browserless):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--ignore-certificate-errors")

    driver = webdriver.Remote(
        command_executor=f"{browserless}/webdriver",
        options=chrome_options
    )
    return driver

def click(driver, name):
    elem = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, name)))
    elem.click()
    return 0

main()
