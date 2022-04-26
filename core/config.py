from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings and Environment Variables

    Args:
        BaseSettings (class): pydantic
    Note:
        default is not .env file
    """

    app_name: str = "Bookmark Service"
    admin_email: str = "test@localhost.ru"
    db_url: str = "localhost.ru"


class Config:
    env_file = ".env"
