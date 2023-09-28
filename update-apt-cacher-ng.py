import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def main():
    parser = argparse.ArgumentParser(description="Update apt-cacher-ng")
    parser.add_argument("--url", required=True, help="URL of the proxy")

    args = parser.parse_args()

    url_argument = args.url
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=400,350")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.binary_location = "/usr/bin/chromium"

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(f"{url_argument}/acng-report.html")
    click(driver, "doImport")
    driver.get(f"{url_argument}/acng-report.html")
    click(driver, "doDownload")
    click(driver, "doMirror")

def click(driver, name):
    elem = driver.find_element(By.NAME, name)
    elem.click()
    return 0

main()
