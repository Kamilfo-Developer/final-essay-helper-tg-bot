import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")

if not os.path.exists(dotenv_path):
    raise OSError(
        ".env file with TOKEN field must exist in the current directory"
    )

load_dotenv(dotenv_path)

API_TOKEN = os.getenv("TOKEN")
