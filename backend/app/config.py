# Здесь будут основные настройки программы, чтение переменных и т.д.

import os
from pathlib import Path

from dotenv import load_dotenv

# Каталог переменных среды, и его чтение при помощи dotenv
env_path = Path(__file__).parents[3] / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    """
    Класс содержащий атрибуты с настройками проекта
    """

    PROJECT_NAME: str = "SMask"
    PROJECT_VERSION: str = "0.0.1"

    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT = os.getenv(
        "POSTGRES_PORT", 5432
    )  # default postgres port is 5432
    POSTGRES_DB = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


setting = Settings()
