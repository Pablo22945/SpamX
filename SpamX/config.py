import os
from os import getenv as env
from SpamX.functions.logger import LOGS
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

API_ID = int(env("API_ID", "29490193"))
if API_ID is None:
    LOGS.error("Please set your API_ID!")
    quit(1)

API_HASH = str(env("API_HASH", "ce5eeb951b072f978b96a03b06b087be"))
if API_HASH is None:
    LOGS.error("Please set your API_HASH!")
    quit(1)

ASSISTANT_TOKEN = str(env("ASSISTANT_TOKEN", "7741082998:AAE-JOvsTZIs-Ybt7ouhAXxlc1PydlNZTwI"))
if ASSISTANT_TOKEN is None:
    LOGS.error("Please set your ASSISTANT_TOKEN!")
    quit(1)

OWNER_ID = int(env("OWNER_ID", "7601457849"))
if OWNER_ID is None:
    LOGS.error("Please set your OWNER_ID!")
    quit(1)

DATABASE_URL = str(env("DATABASE_URL", None))
if DATABASE_URL is None:
    LOGS.error("Please set your DATABASE_URL!")
    quit(1)

LOGGER_ID = str(env("LOGGER_ID", "-1002354034230"))
if LOGGER_ID is None:
    LOGS.error("Please set your LOGGER_ID! (make a private group add assistant in that group & promote as Admin!)")
    quit(1)

# --- ETC
HANDLER = env("HANDLER", ".")
PING_MSG = env("PING_MSG", "!pong")
ALIVE_MSG = env("ALIVE_MSG", None)
ALIVE_MEDIA = env("ALIVE_MEDIA", None)
MULTITASK = env("ALIVE_MEDIA", False)
