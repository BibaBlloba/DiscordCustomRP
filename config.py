from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_ID: str

    @property
    def redis_url(self):
        return self.APP_ID

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()
