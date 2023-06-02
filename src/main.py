# pip freeze | xargs pip uninstall -y
# pip freeze > requirements.txt
# * -- Imports
import os
import sys

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# * -- Variables
title = "IGBOT"  # ? Title
PATH = os.path.realpath(__file__)  # ? Directory path

load_dotenv(dotenv_path=".env")  # ? Load .env file
TEST = os.getenv("TEST")  # ? Test variable

USER_DATA_DIR = f"{PATH}\\data"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f"--headless")
# chrome_options.add_argument(f"--user-data-dir={USER_DATA_DIR}")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)


# * -- Functions


def clearConsole() -> None:  # ? Clear console
    os.system("cls" if os.name == "nt" else "clear")


def test() -> None:
    print(f"[{title}#test] PATH", PATH)
    print(f"[{title}#test] test", TEST)
    print(f"[{title}#test] USER_DATA_DIR", USER_DATA_DIR)


def main() -> None:
    test()

    driver.get("https://www.instagram.com/")
    elem = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # driver.send_keys(Keys.RETURN)

    input(f"[{title}#main] Press Enter to close...")

    driver.close()


#! Main
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        _, _, exc_tb = sys.exc_info()
        print(f"[{title}#__main__] error (line: {exc_tb.tb_lineno}): ", e)
