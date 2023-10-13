from typing import Optional
from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'APP_TITLE'
    description: str = 'DESCRIPTION'
    cat_fund_db: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
