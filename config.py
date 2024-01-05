from dotenv import load_dotenv
import os
from envparse import Env

load_dotenv()
env = Env()

CLIEN_ID = os.environ.get("clien-id", None)
CLIEN_SECRET = os.environ.get("clien-secret", None)
