import os
import pathlib


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(32)

    current_dir = pathlib.Path(__file__).parent.absolute() # TODO: os.path alternative, priority: low
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{current_dir}/users.db"  # Absolute
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MODELS_PATH = f"{current_dir}/models"  # Absolute
    MODEL_NAMES_PRIVATE = sorted([f.name for f in os.scandir(os.path.join(MODELS_PATH, "private")) if f.is_dir()])
    MODEL_NAMES_PUBLIC = sorted([f.name for f in os.scandir(os.path.join(MODELS_PATH, "public")) if f.is_dir()])

    # Both paths below are extended with the model name and the file name at runtime
    DATA_PATH = f"{current_dir}/models/data" # Data storage for local models
    # File server for local model data – set up through web server, as Flask cannot serve files outside the app file structure
    DATA_URL = "https://dev.imgs.ai/local" 

    NS = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]
    DEFAULT_N = "30"
    SIZES = ["32", "64", "96", "128", "160", "192", "224"]
    DEFAULT_SIZE = "128"

    SESSION_COOKIE_SECURE = False # Activate in production
    REMEMBER_COOKIE_SECURE = False # Activate in production

    DEFAULT_USERNAME = "hi@imgs.ai" # Change in production
    DEFAULT_EMAIL = "hi@imgs.ai" # Change in production
    DEFAULT_PASSWORD = "hi@imgs.ai" # Change in production
