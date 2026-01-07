from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GOOGLE_TOKEN_ID: str = "hhytju7ri87"
    SQLITE_DB_NAME: str = 'pomodoro.db'
