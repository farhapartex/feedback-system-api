from utils import FileManager
import os
import logging

# Statement for enabling the development environment
# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_PATH = os.path.abspath(".")

logging.basicConfig(filename='logger_files/demo.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

settings_json_path = os.path.join(PROJECT_PATH, "settings.json")
settings_json = FileManager.read_json(settings_json_path)

DEBUG = settings_json.get("DEBUG", False)

DATABASE = settings_json.get("DATABASE", {})
DB_NAME = DATABASE.get("name", "")
DB_USER = DATABASE.get("user", "")
DB_PASSWORD = DATABASE.get("password", "")
DB_HOST = DATABASE.get("host", "")
DB_PORT = DATABASE.get("port", "")

DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

