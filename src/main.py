# pip freeze | xargs pip uninstall -y
# pip freeze > requirements.txt
# * -- Imports
import os
import sys
from dotenv import load_dotenv

# * -- Variables
title = "IGBOT"  # ? Title
path = os.path.dirname(__file__)  # ? Directory path

load_dotenv(dotenv_path=".env")  # ? Load .env file
test = os.getenv("TEST")  # ? Test variable

# * -- Functions


def clearConsole() -> None:  # ? Clear console
    os.system("cls" if os.name == "nt" else "clear")


def main() -> None:
    print(f"[{title}#main] test", test)


#! Main
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        _, _, exc_tb = sys.exc_info()
        print(f"[{title}#__main__] error (line: {exc_tb.tb_lineno}): ", e)
