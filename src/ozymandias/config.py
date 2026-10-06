from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Lê também o arquivo .env; ignora variáveis que não são campos desta classe
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Obrigatória: sem ela, a aplicação não inicia
    database_url: str


# Uma instância única, importada pelo resto da aplicação
settings = Settings()
