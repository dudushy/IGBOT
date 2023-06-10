# pip freeze | xargs pip uninstall -y
# pip freeze > requirements.txt
# * -- Imports
import os
import sys
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# * -- Variables
title = "IGBOT"  # ? Title
PATH = os.path.realpath(__file__)  # ? Directory path

DOT_ENV_PATH = f"{PATH.replace('main.py', '')}..\\.env"  # ? .env file path
load_dotenv(dotenv_path=DOT_ENV_PATH, override=True)  # ? Load .env file

TEST = os.getenv("TEST")  # ? Test variable
USERNAME = os.getenv("USERNAME")  # ? Username variable
PASSWORD = os.getenv("PASSWORD")  # ? Password variable

USER_DATA_DIR = f"{PATH}\\data"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f"--headless")
# chrome_options.add_argument(f"--user-data-dir={USER_DATA_DIR}")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

DRIVER = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)
DRIVER_WAIT = WebDriverWait(DRIVER, 20)


# * -- Functions


def clearConsole() -> None:  # ? Clear console
    os.system("cls" if os.name == "nt" else "clear")


def checkVars() -> None:
    print(f"[{title}#checkVars] PATH", PATH)
    print(f"[{title}#checkVars] DOT_ENV_PATH", DOT_ENV_PATH)
    print(f"[{title}#checkVars] TEST", TEST)
    print(f"[{title}#checkVars] USER_DATA_DIR", USER_DATA_DIR)
    print(f"[{title}#checkVars] USERNAME", USERNAME)
    print(f"[{title}#checkVars] PASSWORD", PASSWORD)


def main() -> None:
    try:
        # clearConsole()
        checkVars()

        # ? Load instagram.com
        DRIVER.get("https://www.instagram.com/")
        print(f"[{title}#main] get instagram.com")

        # ? Insert username and password
        print(f"[{title}#main] searching username input...")
        element = DRIVER_WAIT.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
        )
        print(f"[{title}#main] found username input")
        element.send_keys(USERNAME)
        print(f"[{title}#main] typed username")

        print(f"[{title}#main] searching password input...")
        element = DRIVER_WAIT.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))
        )
        print(f"[{title}#main] found password input")
        element.send_keys(PASSWORD)
        print(f"[{title}#main] typed password")

        # ? Login and wait
        element.send_keys(Keys.ENTER)
        print(f"[{title}#main] sent ENTER")
        time.sleep(5)

        # ? Dissmiss save login info
        # print(f"[{title}#main] searching info not now button...")
        # element = DRIVER_WAIT.until(EC.element_to_be_clickable(
        #     (By.XPATH, '//*[@id="mount_0_0_mV"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'))
        # )
        # print(f"[{title}#main] found info not now button")
        # element.click()
        # print(f"[{title}#main] clicked info not now button")

        # ? Dissmiss notifications
        # print(f"[{title}#main] searching notifications not now button...")
        # element = DRIVER_WAIT.until(EC.element_to_be_clickable(
        #     (By.XPATH, '//*[@id="mount_0_0_1a"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'))
        # )
        # print(f"[{title}#main] found notifications not now button")
        # element.send_keys(Keys.ENTER)
        # print(f"[{title}#main] clicked notifications not now button")

        # ? Click create button
        print(f"[{title}#main] searching create button...")
        element = DRIVER_WAIT.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mount_0_0_hA"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a/div/div[1]/div/div/svg'))
        )
        print(f"[{title}#main] found create button")
        element.click()
        print(f"[{title}#main] clicked create button")

        # ? Close
        input(f"[{title}#main] Press Enter to close...")

        print(f"[{title}#main] closing...")
        DRIVER.close()
        print(f"[{title}#main] closed")
    except Exception as e:
        _, _, exc_tb = sys.exc_info()
        print(f"[{title}#main] error (line: {exc_tb.tb_lineno}): ", e)


#! Main
if __name__ == "__main__":
    main()
