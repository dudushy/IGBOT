# pip freeze | xargs pip uninstall -y
# pip freeze > requirements.txt
# * -- Imports
import os
import sys

from dotenv import load_dotenv
from instagrapi import Client

# * -- Variables
title = "IGBOT"  # ? Title
PATH = os.path.realpath(__file__)  # ? Directory path

DOT_ENV_PATH = f"{PATH.replace('main.py', '')}..\\.env"  # ? .env file path
load_dotenv(dotenv_path=DOT_ENV_PATH, override=True)  # ? Load .env file

TEST = os.getenv("TEST")  # ? Test variable
USERNAME = os.getenv("USERNAME")  # ? Username variable
PASSWORD = os.getenv("PASSWORD")  # ? Password variable


# * -- Functions


def clearConsole() -> None:  # ? Clear console
    os.system("cls" if os.name == "nt" else "clear")


def checkVars() -> None:
    print(f"[{title}#checkVars] PATH", PATH)
    print(f"[{title}#checkVars] DOT_ENV_PATH", DOT_ENV_PATH)
    print(f"[{title}#checkVars] TEST", TEST)
    print(f"[{title}#checkVars] USERNAME", USERNAME)
    print(f"[{title}#checkVars] PASSWORD", PASSWORD)

def main() -> None:
    try:
        # clearConsole()
        checkVars()

        print(f"[{title}#main] init")

        cl = Client()
        cl.login(USERNAME, PASSWORD)

        media = cl.photo_upload(
            f"{PATH.replace('main.py', '')}\\assets\\images\\sample.jpg",
            "Test ❤ #test @test",
            extra_data={
                "custom_accessibility_caption": "alt text example",
                "like_and_view_counts_disabled": 1,
                "disable_comments": 1,
            }
        )
        media.dict()

        print(f"[{title}#main] end")
    except Exception as e:
        _, _, exc_tb = sys.exc_info()
        print(f"[{title}#main] error (line: {exc_tb.tb_lineno}): ", e)


#! Main
if __name__ == "__main__":
    main()
